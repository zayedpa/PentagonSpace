class passengerplane:
    def takeoff(self):
        print("pp is takeoff")
    def fly(self):
        print("pp is flying")
    def land(self):
        print("pp is landing")
    def carry_p(self):
        print("pp carries p")
class cargoplane:
    def takeoff(self):
        print("cp is takeoff")
    def fly(self):
        print("cp is flying")
    def land(self):
        print("cp is landing")
    def carry_g(self):
        print("cp carries g")
class fighterplane:
    def takeoff(self):
        print("fp is takeoff")
    def fly(self):
        print("fp is flying")
    def land(self):
        print("fp is landing")
    def carry_w(self):
        print("fp carries w")

p1=passengerplane()
c1=cargoplane()
f1=fighterplane()
p1.takeoff()
p1.fly()
p1.land()
p1.carry_p()

c1.takeoff()
c1.fly()
c1.land()
c1.carry_g()

f1.takeoff()
f1.fly()
f1.land()
f1.carry_w()