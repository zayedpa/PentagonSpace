def fun1():
    print("entering fun1")
    try:
        fun2()
    except Exception as e:
        print("error occured in fun1")
    print("leaving fun1")
def fun2():
    print("entering fun2")
    res=10/0
    print(res)
    print("leaving fun2")
print("program strated")
fun1()
print('program ended')