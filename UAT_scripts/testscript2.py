#!/usr/bin/python3
def words_count(filename):
    with open(filename, 'r') as file:
        strg = file.read()
        number = len(strg.split())
        return number
print(words_count("testscript.py"))

a = [1, 2, 3]
b = (4, 5, 8)
for i, j in zip(a,b):
    print(i + j)
