from PIL import Image
import pytesseract
import os
import file_handler

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"  # pytesseract path


def ocr():
    photos = file_handler.file_handler()  # "set" with all photos to be processed
    text_dict = {}  # key = filename, value = text
    for i in photos:
        path = file_handler.photos_path() + "/" + i
        image = Image.open(path)
        text = pytesseract.image_to_string(image)
        filename, extension = os.path.splitext(i)  # separate filename from extension
        temp_dict = {filename : text}
        text_dict.update(temp_dict)

    return text_dict  # add text handling
