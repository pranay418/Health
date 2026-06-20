
import pytesseract
import sys
from pdf2image import convert_from_bytes
from PIL import Image

# Set tesseract path on Linux cloud deployments
if sys.platform.startswith('linux'):
    pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

def extract_text_from_image(image):
    return pytesseract.image_to_string(image)

def extract_text_from_pdf(pdf_file):
    # Convert uploaded file-like object bytes directly
    pages = convert_from_bytes(pdf_file.read())
    text = ""
    for page in pages:
        text += pytesseract.image_to_string(page)
    return text
