class Bike:
    def __init__(self):
        self.brand="KTM"
    def __move(self):
        print("bike is running")
    def helper(self):
        self.__move()
b1=Bike()
b1.helper()