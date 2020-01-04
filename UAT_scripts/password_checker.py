#!/usr/bin/python3
while True:
    psw = input("Enter new password: ")
    if any(i.isdigit() for i in psw) and any(i.isupper() for i in psw) and len(psw) >= 5:
        print("Password is fine")
        break
    else:
        print("Password is not fine")
        print("Password must contain a Upper case character, number and 5 char long. Please try again \n")
