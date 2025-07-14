class Person:
    def __init__(self):
        self.__name=""
    def setter(self,value):
        self.__name=value
    def getter(self):
        return self.__name
p1=Person()
p1.setter("rumaan")
res=p1.getter()
print(res)
p1.setter("zayed")
res1=p1.getter()
print(res1)
p1.setter("asgy")
res2=p1.getter()
print(res2)
