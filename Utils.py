import os

def get_string_list(input_list, indent=0):
    indent_string = indent*" " + "\n"
    input_list_string = [str(item) for item in input_list]
    string = indent_string.join(input_list_string)
    string = "\n"*(len(input_list) != 0) + string
    return string

def make_folder(path):
    if not os.path.isdir(path):
        os.mkdir(path)
