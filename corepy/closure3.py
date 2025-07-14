def outer(): #using 3 functions
    print("inside outer")
    def inner():
        print("inside inner")
        def innerm():
            print("inside innerm")
        return innerm
    ref1=inner()    
    ref1()    
    return inner
ref2=outer()
ref2()