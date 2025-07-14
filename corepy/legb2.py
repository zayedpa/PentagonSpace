def outer():
    a=10
    b=20
    print(a)
    print(b)
    print(c)
    def inner():
        c=100
        print(c)
    inner()
outer()