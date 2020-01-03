#!/usr/bin/python
a = ["1", 1, "1", 2]
a = list(set(a))
print(a)
from collections import OrderedDict
c = ["1", 1, "1", 2]
c = list(OrderedDict.fromkeys(c))
print(c)
d = ["1", 1, "1", 2]
b = []
for i in d:
    if i not in b:
        b.append(i)
print(b)
