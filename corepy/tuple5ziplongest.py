from itertools import zip_longest
names=["virat","dhoni","gill","abd"]
j_no=[18,7,77,17]
country=["ind","ind","ind","sa"]
runs=[1000,3000]
res=list(zip_longest(names,j_no,country,runs,fillvalue="#"))  #type casting
print(res)