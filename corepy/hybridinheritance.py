# hybrid inheritance using hierarchical inheritance and multiple inheritance



class animal:
    def move(self):
        print("animal is moving")
class mammal(animal):
    def feed(self):
        print("mammal is feeding milk")
class bird(animal):
    def fly(self):
        print("bird is flying")
class bat(mammal,bird):
    def both(self):
        print("bat is both mammal and bird")

b1=bat()
b1.both()
b1.fly()
b1.feed()
b1.move()