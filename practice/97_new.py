#!/usr/bin/python

file = open("copy_data_to_file.txt", "w")

while True:
    text = input("Enter value: ")
    if text == "CLOSE":
        file.close()
        break
    if text == "SAVE":
        for i in lines:
            file.write(lines + "\n")
        continue
    else:
        lines = file.readlines()
        continue
