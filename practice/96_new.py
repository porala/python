#!/usr/bin/python

file = open("copy_data_to_file.txt", "a+")

while True:
    text = input("Enter value: ")
    if text == "CLOSE":
        file.close()
        break
    else:
        file.write(text + "\n")
