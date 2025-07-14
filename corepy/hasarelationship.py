class Radio:
    def turnon(self,x):
        if x==1:
            print("radio is on")
        else:
            print("radio is off")
class Car:
    def __init__(self,max,min):
        self.cmax=max
        self.cmin=min
        self.r=Radio()

c1=Car(180,20)
print(c1.cmax)
print(c1.cmin)
c1.r.turnon(1)
c1.r.turnon(0)