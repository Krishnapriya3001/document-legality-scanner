import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image_path):
    image = cv2.imread(image_path)

    text = pytesseract.image_to_string(image)

    return text

legal_keywords = [
    "agreement",
    "certificate",
    "government",
    "license",
    "signature",
    "date"
]

def check_document(text):

    text = text.lower()

    found = []

    for word in legal_keywords:
        if word in text:
            found.append(word)

    return found