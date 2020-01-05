from googletrans import Translator


def translator(text_dict, language):

    for i in text_dict:
        text_only = text_dict[i]  # i = key, text_dict[i] = value
        t = Translator()
        trans = t.translate(text_only, dest = language)
        trans = trans.text
        text_dict[i] = trans

    return text_dict
