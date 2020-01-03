#!/usr/bin/python3
import time
value1 = 0 
while True:
    value1 = value1 + 1
    print("Hello")
    time.sleep(value1)
    if value1 == 3:
        print("End of the loop")
        break
