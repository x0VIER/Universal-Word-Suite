import os
import sys
import argparse
from pathlib import Path
import html
import re

# --- CONFIGURATION ---
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TIMING_RE = re.compile(r"^(?P<start>\d\d:\d\d:\d\d\.\d{3}) --> (?P<end>\d\d:\d\d:\d\d\.\d{3})")
TAG_RE = re.compile(r"<[^>]+>")

def clean_text(text: str) -> str:
    text = html.unescape(text)
    text = TAG_RE.sub("", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def parse_vtt(path: Path) -> list[tuple[str, str, str]]:
    entries: list[tuple[str, str, str]] = []
    if not path.exists():
        print(f"Error: File not found at {path}")
        return []
        
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    i = 0
    while i < len(lines):
        match = TIMING_RE.match(lines[i].strip())
        if not match:
            i += 1
            continue
        start = match.group("start")
        end = match.group("end")
        i += 1
        text_lines: list[str] = []
        while i < len(lines) and lines[i].strip():
            text_lines.append(lines[i].strip())
            i += 1
        text = clean_text(" ".join(text_lines))
        if text:
            entries.append((start, end, text))
    return dedupe_entries(entries)

def dedupe_entries(entries: list[tuple[str, str, str]]) -> list[tuple[str, str, str]]:
    cleaned: list[tuple[str, str, str]] = []
    previous_text = ""
    for start, end, text in entries:
        if text == previous_text:
            continue
        cleaned.append((start, end, text))
        previous_text = text
    return cleaned

def write_reading_copy(entries: list[tuple[str, str, str]], path: Path) -> None:
    paragraphs: list[str] = []
    current: list[str] = []
    current_start = ""
    last_minute = -1

    for start, _end, text in entries:
        minute = int(start[3:5]) + int(start[0:2]) * 60
        if not current:
            current_start = start[:8]
            last_minute = minute
        should_break = len(" ".join(current)) > 900 or minute - last_minute >= 3
        if should_break:
            paragraphs.append(f"[{current_start}] {' '.join(current)}")
            current = []
            current_start = start[:8]
        current.append(text)
        last_minute = minute

    if current:
        paragraphs.append(f"[{current_start}] {' '.join(current)}")

    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write("Raw Capture Transcript\n")
        handle.write("======================\n\n")
        handle.write(
            "Source: YouTube captions captured from browser session.\n"
            "Status: Local extraction only.\n\n"
        )
        for paragraph in paragraphs:
            handle.write(paragraph + "\n\n")

def main():
    parser = argparse.ArgumentParser(description="Raw Capture YT: Transcript Extraction Tool")
    parser.add_argument("input", help="Path to the .vtt caption file")
    parser.add_argument("--name", help="Output filename (optional)", default="transcript_output")
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    output_path = OUTPUT_DIR / f"{args.name}.txt"
    
    print(f"Processing: {input_path}")
    entries = parse_vtt(input_path)
    
    if entries:
        write_reading_copy(entries, output_path)
        print(f"Success! Output saved to: {output_path}")
    else:
        print("No valid transcript entries found.")

if __name__ == "__main__":
    main()
