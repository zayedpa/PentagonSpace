def outer():
    a=10
    b=20
    print(a)
    print(b)
    def inner():
        
        a=15
        b=25
        print(a)
        print(b)
    return inner
ref=outer()
ref()