#!/usr/bin/python3
d = dict(weather = "clima", earth = "terra", rain = "chuva")
def vocabulary(word):
    try:
        return d[word]
    except KeyError:
        return "That bad word"

word = input("Enter word: ").lower()
print(vocabulary(word))
