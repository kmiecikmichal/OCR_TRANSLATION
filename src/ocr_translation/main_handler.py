import file_handler
import ocr
import text_to_file

def main_handler():
    photos_path = file_handler.photos_path()
    text_path = file_handler.text_path()
    photos = file_handler.file_handler()  # "set" with all photos to be processed
    text_dict = ocr.ocr(photos, photos_path)
    text_to_file.text_to_file(text_dict, text_path)
