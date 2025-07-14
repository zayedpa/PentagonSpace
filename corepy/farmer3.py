class farmer:
    r=2.5    #static variable
    def __init__(self,p,t):
        self.principle=p
        self.time=t
    def loan(self):
        si=(self.principle*self.time*farmer.r)/100
        print(si)
f1=farmer(100000,3)
f1.loan()
print(farmer.r)
f2=farmer(200000,5)
f2.loan()