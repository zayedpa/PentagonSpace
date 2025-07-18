try:
    a=int(input("enter num1"))
    b=int(input("enter num2"))
    res=a/b
    print(res)
except Exception as e:
    print("error occured")
    print(e.__str__())   # or print(e)
else:
    print("pgm run successfully")