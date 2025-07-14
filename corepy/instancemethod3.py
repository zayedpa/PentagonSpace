#with parameter no return value
class calci:
    def __init__(self):
        self.brand='casio'
        self.cost=1500
    def add(self,a,b):     #a,b are formal parameter
        c=a+b
        print(c)
c1=calci()
print(c1.brand)
print(c1.cost)
x=10    #  x,y are actual parameter
y=20
c1.add(x,y)