try:
    a=int(input("enter num1"))
    b=int(input("enter num2"))
    res=a/b
    print(res)
except (ValueError,ZeroDivisionError) as e:
    print("it is value error or zde")
except Exception as e:
    print("error occured")