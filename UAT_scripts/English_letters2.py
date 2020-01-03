#!/usr/bin/python3
import string
for letter in string.ascii_lowercase:
    with open(letter + ".txt", "w") as newfile:
        newfile.write(letter)
