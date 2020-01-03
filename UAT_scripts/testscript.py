#!/usr/bin/python3
for x in range(1,30):
    if x % 2 == 0:
        pass
    else:
        print("This is odd number", x)
from pprint import pprint
d = {"a":list(range(1, 11)), "b":list(range(11, 21)), "c":list(range(21, 31))}
pprint(d)
import string
for letter in string.ascii_lowercase:
    print(letter)

def acceleration(v1, v2, t1, t2):
    a = float(v2 - v1) / float(t2 - t1)
    return a
print(acceleration(0,10,0,20))
print(acceleration(990,50,38830,20))
def foo(b, a=100):
    return a + b
print(foo(10))
name = str(input("Enter your name "))
print(len(name.split()))
