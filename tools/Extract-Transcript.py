import os
import sys
import argparse
from pathlib import Path
import html
import re
import subprocess

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

def transcribe_audio(input_path: Path, model_size="base") -> list[tuple[str, str, str]]:
    """Local transcription using faster-whisper. Works on any video/audio."""
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        print("Error: faster-whisper not installed. Run 'pip install faster-whisper'")
        return []

    print(f"Loading Whisper model ({model_size})...")
    model = WhisperModel(model_size, device="cpu", compute_type="int8") # CPU-friendly default
    
    print(f"Transcribing audio from: {input_path}")
    segments, _ = model.transcribe(str(input_path), beam_size=5)
    
    entries = []
    for segment in segments:
        start = format_timestamp(segment.start)
        end = format_timestamp(segment.end)
        entries.append((start, end, segment.text.strip()))
    
    return entries

def format_timestamp(seconds: float) -> str:
    td = float(seconds)
    hours = int(td // 3600)
    minutes = int((td % 3600) // 60)
    secs = int(td % 60)
    msecs = int((td % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{secs:02}.{msecs:03}"

def write_reading_copy(entries: list[tuple[str, str, str]], path: Path) -> None:
    paragraphs: list[str] = []
    current: list[str] = []
    current_start = ""
    last_minute = -1

    for start, _end, text in entries:
        # Expected format: HH:MM:SS.mmm
        try:
            minute = int(start[3:5]) + int(start[0:2]) * 60
        except:
            minute = 0
            
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
        handle.write("Deep Transcript Extraction\n")
        handle.write("==========================\n\n")
        handle.write(
            "Source: Processed locally for maximum fidelity.\n"
            "Method: Transcription/Extraction via Universal Word Suite.\n\n"
        )
        for paragraph in paragraphs:
            handle.write(paragraph + "\n\n")

def main():
    parser = argparse.ArgumentParser(description="Extract-Transcript: High-Fidelity Capture Tool")
    parser.add_argument("input", help="Path to the .vtt file OR video/audio file")
    parser.add_argument("--mode", choices=["caption", "audio"], default="caption", 
                        help="Mode: 'caption' for VTT files, 'audio' for local AI transcription")
    parser.add_argument("--name", help="Output filename", default="transcript_output")
    parser.add_argument("--model", default="base", help="Whisper model size (for audio mode)")
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    output_path = OUTPUT_DIR / f"{args.name}.txt"
    
    if args.mode == "caption":
        print(f"Mode: Caption Extraction")
        entries = parse_vtt(input_path)
    else:
        print(f"Mode: Local AI Transcription (No captions required)")
        entries = transcribe_audio(input_path, model_size=args.model)
    
    if entries:
        write_reading_copy(entries, output_path)
        print(f"Success! Output saved to: {output_path}")
    else:
        print("No valid transcript entries found or transcription failed.")

if __name__ == "__main__":
    main()
