import unittest
from src.ocr_translation import file_handler
from src.ocr_translation import ocr
# Command to run the test: python -m unittest tests.test_file_handler


class TestFileHandler(unittest.TestCase):
    photos_path = file_handler.photos_path()
    text_path = file_handler.text_path()
    photos_set = file_handler.file_handler()
    text_dict = ocr.ocr(photos_set, photos_path)

    def test_photos_path(self):
        path = self.photos_path
        self.assertTrue(path, "Empty photos path")

    def test_text_path(self):
        path = self.text_path
        self.assertTrue(path, "Empty text path")

    def test_photos_set(self):
        p_set = self.photos_set
        self.assertTrue(p_set, "Empty photos set")

    def test_is_ocr_dict(self):
        texts = self.text_dict
        self.assertIsInstance(texts, dict)

    def test_ocr_dict_content(self):
        texts = self.text_dict
        self.assertEqual(texts, {"sample": 'This is the first line of this text example.  This is the second ' 'line of the same text.'})