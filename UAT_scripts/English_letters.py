#!/usr/bin/python3
import string
with open("letters.filename", "w") as file:
    for letter in string.ascii_lowercase:
        file.write(letter + "\n")
