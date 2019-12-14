import os
import sys


def photos_path():
    path = os.path.abspath(os.path.dirname(__file__)) + "/photos"
    return path


def text_path():
    path = os.path.abspath(os.path.dirname(__file__)) + "/text"
    return path


def file_handler():
    photos_abs_path = photos_path()
    photos = set()
    for i in os.listdir(photos_abs_path):
        if i.endswith(".jpg") or i.endswith(".png") or i.endswith(".bmp"):
            photos.add(i)

    text_abs_path = text_path()
    text = set()
    for i in os.listdir(text_abs_path):
        if i.endswith(".txt"):
            text.add(i)

    for i in photos.copy():
        filename_p, extension_p = os.path.splitext(i)
        for j in text:
            filename_t, extension_t = os.path.splitext(j)
            if filename_p == filename_t:
                photos.remove(i)

    try:
        if len(photos) == 0:
            raise Exception("Warning: List of untranslated pictures is empty")
    except Exception as exc:
        print(exc)
        sys.exit(0)

    return photos
