def fun1():
    print("inside fun1")
def fun2():
    print("inside fun2")
ptr1=fun1
ptr2=fun2
ptr1()
ptr2()