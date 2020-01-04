#!/usr/bin/python3
while True:
    username = input("Enter username: ")
    with open("users.txt", 'r') as file:
        users = file.readlines()
        users = [i.strip("\n") for i in users]
    if username in users:
        print("Username exists. Please try again")
        continue
    else:
        break
