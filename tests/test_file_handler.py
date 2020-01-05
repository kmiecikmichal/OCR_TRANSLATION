import unittest
from src.ocr_translation import file_handler
# Command to run the test: python -m unittest tests.test_file_handler


class TestFileHandler(unittest.TestCase):
    photos_path = file_handler.photos_path()
    text_path = file_handler.text_path()
    photos_set = file_handler.file_handler()

    def test_photos_path(self):
        path = self.photos_path
        self.assertTrue(path, "Empty photos path")

    def test_text_path(self):
        path = self.text_path
        self.assertTrue(path, "Empty text path")

    def test_photos_set(self):
        p_set = self.photos_set
        self.assertTrue(p_set, "Empty photos set")
