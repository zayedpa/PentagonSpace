class animal:
    def eat(self):
        print("animal is eating")
    def sleep(self):
        print("animal is sleeping")
    def hunt(self):
        print("animal is hunting")
class dog(animal):
    pass
class lion(animal):
    pass
class tiger(animal):
    pass
d1=dog()
l1=lion()
t1=tiger()

d1.eat()
d1.sleep()
d1.hunt()

l1.eat()
l1.sleep()
l1.hunt()

t1.eat()
t1.sleep()
t1.hunt()