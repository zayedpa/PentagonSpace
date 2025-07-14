class laptop():
    def __init__(self):   #instance method
        self.brand='hp'
        self.cost=1500
    def on(self):
        print("laptop is on")
    @staticmethod       #static method
    def gaming():
        print("laptop is doing games")
    @classmethod       #class method
    def off(cls):
        print("laptop is turned off")
l1=laptop()      #a reference variable is needed to call instance method
print(l1.brand)
l1.on()
laptop.gaming()   #staticmethod and classmethod dont need reference 
laptop.off()      #they can be called with class name
print(l1.cost)
