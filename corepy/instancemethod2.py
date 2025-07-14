#no parameter with return value
class calci:
    def __init__(self):
        self.brand='casio'
        self.cost=1500
        self.model=900
    def add(self):
            a=15
            b=25
            c=a+b
            return c
    def sub(self):
            w=50
            x=40
            v=w-x
            return v
            
c1=calci()
print(c1.brand)
print(c1.model)
print(c1.cost)
res=c1.add()
print(res)
rev=c1.sub()
print(rev)
