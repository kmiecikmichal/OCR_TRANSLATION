from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"


def image_to_str():
    image_file = "sample.jpg"  # add list of all images in repo
    image = Image.open(image_file)
    text = pytesseract.image_to_string(image)
    return text  # add text handling
