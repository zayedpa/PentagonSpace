from  math import pi
#pi=10   #global scope
def outer():
    #pi=20  #enclosed scopre
    def inner():
        #pi=15  #local scope
        print(pi)
    inner()
outer()