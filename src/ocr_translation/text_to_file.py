def text_to_file(text_dict, text_path):
    for i in text_dict:
        filename = text_path + "/" + i + ".txt"  # i = key
        text = text_dict[i]  # value
        with open(filename, "w+") as f:
            f.write(text)
