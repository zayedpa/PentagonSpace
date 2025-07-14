class dog:
    def __init__(self):
        self.name="charlie"  #inside the class inside the constructor
        self.breed="husky"
    def bark(self):
        print('dog is barking')
        self.color="black"   #inside the class inside the method
d1=dog()
print(d1.breed)
d1.bark()
print(d1.color)
d1.age=10      #outside the class
print(d1.age)



#this program shows to declare instance variable in three formats