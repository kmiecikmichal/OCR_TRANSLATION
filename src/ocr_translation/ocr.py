from PIL import Image
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"  # pytesseract path


def ocr(photos, photos_path):
    text_dict = {}  # key = filename, value = text
    for i in photos:
        photos_path = photos_path + "/" + i
        image = Image.open(photos_path)
        text = pytesseract.image_to_string(image)
        filename, extension = os.path.splitext(i)  # separate filename from extension
        temp_dict = {filename : text}
        text_dict.update(temp_dict)

    return text_dict  # add text handling
