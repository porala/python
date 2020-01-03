#!/usr/bin/python3
def replace_text(filename):
    with open(filename, 'r') as file:
        text = file.read()
        text = text.replace(",", " ")
        str_ltn = text.split(" ")
        return len(str_ltn)
print(replace_text("replace_text.py"))
