import copy
l=[10,20,30,["kalyan","varun"],40]
print(l)
l1=copy.deepcopy(l)
print(l)
print(l1)
del l[3][1]
print(l)
print(l1)