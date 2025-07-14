a=10
def outer():
    global a
    a=100
    b=200
    print(a)
    print(b)
def inner():
    c=300
    print(a)
    print(c)
print(a)
outer()
inner()

