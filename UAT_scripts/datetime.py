#!/usr/bin/python
from datetime import datetime
age = int(input("Enter your age: "))
year_birth = datetime.now().year - age
print("Your birth year is : ", year_birth)
