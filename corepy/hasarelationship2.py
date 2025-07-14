class brain:
    def active(self,x):
        if x==1:
            print("brain is active")
        else:
            print("brain is not active")

class car:
    def __init__(self,name):
        self.cname=name
    def getcar(self):
        print("car is getting ready")

class person:
    def __init__(self,name):
        self.pname=name
        self.b=brain()
        print("brain is ready")
        self.c=""
    def hascar(self,p):
        self.c=p

p1=person("jack")
print(p1.pname)
p1.b.active(1)
p1.b.active(2)
c1=car("bmw")
print(c1.cname)
p1.hascar(c1)
c1.getcar()

del p1
print(c1.cname)

c1.getcar()

print(p1.pname)






