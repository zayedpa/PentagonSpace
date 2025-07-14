def outer():
    a=10
    b=20   #non local variable
    print(a)
    print(b)    
    def inner():
        c=120
        d=150  #local variable
        print(c)
        print(d)
    inner()
outer()
