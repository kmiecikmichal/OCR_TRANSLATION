from PIL import Image
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"  # pytesseract path


def ocr(photos, photos_path):
    text_dict = {}  # key = filename, value = text
    for i in photos:
        photos_path_file = photos_path + "/" + i
        image = Image.open(photos_path_file)
        text = pytesseract.image_to_string(image)
        text = text.replace("\n", " ")  # delete newlines
        filename, extension = os.path.splitext(i)  # separate filename from extension
        temp_dict = {filename : text}
        text_dict.update(temp_dict)

    return text_dict  # add text handling
