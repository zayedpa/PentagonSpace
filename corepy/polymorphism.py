class plane:
    def takeoff(self):
        print("plane is takeoff")
    def fly(self):
        print("plane is flying")
    def land(self):
        print("plane is landing")

class passenger(plane):
    def carry_p(self):
        print("pp carries p")
class cargo(plane):
    def carry_g(self):
        print("cp carries g")
class fighter(plane):
    def carry_w(self):
        print("fp carries w")

p1=passenger()
c1=cargo()
f1=fighter()

def allowPlane(ref):
    ref.takeoff()
    ref.fly()
    ref.land()

allowPlane(p1)
p1.carry_p()
allowPlane(c1)
c1.carry_g()
allowPlane(f1)
f1.carry_w()
