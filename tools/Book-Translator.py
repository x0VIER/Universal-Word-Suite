import os
import sys
import re
import argparse
from pathlib import Path
from deep_translator import GoogleTranslator

# --- CONFIGURATION ---
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

class BookTranslator:
    """High-fidelity OCR and translation engine for physical/digital books."""
    
    def __init__(self, source_lang='es', target_lang='en'):
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.translator = GoogleTranslator(source=source_lang, target=target_lang)
        self.ocr_reader = None 
        
    def _get_ocr(self):
        if self.ocr_reader is None:
            import easyocr
            print("[Book-Translator] Initializing High-Fidelity OCR Engine...")
            self.ocr_reader = easyocr.Reader([self.source_lang, self.target_lang])
        return self.ocr_reader

    def clean_text(self, text):
        """Removes common OCR artifacts and formatting noise."""
        # Generic cleanup patterns
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def process(self, image_folder, output_name):
        """Processes a folder of page images into a translated document."""
        print(f"[Book-Translator] Processing images from {image_folder}...")
        reader = self._get_ocr()
        output_path = OUTPUT_DIR / f"{output_name}_FINAL.txt"
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(f"Translation: {output_name}\n")
            f.write("="*40 + "\n\n")

        # Sort images numerically if possible
        images = sorted(list(Path(image_folder).glob("*.png")), 
                        key=lambda x: int(re.search(r'\d+', x.name).group()) if re.search(r'\d+', x.name) else x.name)
        
        if not images:
            print("No .png images found in the specified folder.")
            return

        for i, img_path in enumerate(images, 1):
            print(f"[Book-Translator] OCR Processing Page {i}/{len(images)}...")
            result = reader.readtext(str(img_path), detail=0)
            raw_text = " ".join(result)
            
            if not raw_text.strip(): continue
            
            translated_text = self.translator.translate(raw_text)
            translated_text = self.clean_text(translated_text)
            
            with open(output_path, "a", encoding="utf-8") as f:
                f.write(f"--- PAGE {i} ---\n")
                f.write(translated_text + "\n\n")
        
        print(f"[Book-Translator] Document Complete: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Book-Translator: High-Fidelity OCR & Translation Tool")
    parser.add_argument("input", help="Path to the folder containing page images")
    parser.add_argument("--name", help="Output filename", default="book_translation")
    parser.add_argument("--src", default="es", help="Source language (default: es)")
    parser.add_argument("--dest", default="en", help="Target language (default: en)")
    
    args = parser.parse_args()
    
    engine = BookTranslator(source_lang=args.src, target_lang=args.dest)
    engine.process(args.input, args.name)

if __name__ == "__main__":
    main()
