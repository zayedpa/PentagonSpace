def outer():
    a=10  #non local variables
    b=20
    print(a)
    print(b)
    def inner():
        nonlocal a  #to modify the non local variable
        a=100
        b=200  #local variables
        print(a)
        print(b)
    print(a)
    inner()
    print(a)
outer()