#with parameter with return value

class calci:
    def __init__(self):
        self.brand='casio'
        self.cost=1500
    def add(self,a,b):
        c=a+b
        return c
c1=calci()
print(c1.brand)
print(c1.cost)
x=10
y=20
res=c1.add(x,y)
print(res)


