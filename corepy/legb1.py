def outer():
    a=10
    b=20
    print(a)
    print(b)
    def inner():
        c=200
        print(a)
        print(c)
    inner()
outer()