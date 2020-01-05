import file_handler
import ocr
import text_to_file
import translator


def main_handler():
    photos_path = file_handler.photos_path()
    text_path = file_handler.text_path()
    photos = file_handler.file_handler()  # "set" with all photos to be processed
    text_dict = ocr.ocr(photos, photos_path)
    language = "pl"  # destined language
    translated_text_dict = translator.translator(text_dict, language)
    text_to_file.text_to_file(translated_text_dict, text_path)
