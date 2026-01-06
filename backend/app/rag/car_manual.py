from PyPDF2 import PdfReader
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
PDF_PATH = BASE_DIR.parent / "docs" / "car_manual.pdf"

def load_car_manual_chunks() -> list[str]:
    reader = PdfReader(PDF_PATH)
    raw_text = ""
    for page in reader.pages:
        if page.extract_text():
            raw_text += page.extract_text() + "\n"
    return [c.strip() for c in raw_text.split("\n\n") if c.strip()]

CAR_MANUAL_CHUNKS = load_car_manual_chunks()