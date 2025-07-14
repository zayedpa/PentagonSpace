def fun1():
    a=10
    b=20
    print(a)
    print(b)
    def fun2():
        c=30
        d=40
        print(c)
        print(d)
   
        def fun3():
            e=50
            f=60
            print(e)
            print(f)
        fun3()
    fun2()
fun1()
