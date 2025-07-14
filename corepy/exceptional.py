a=int(input("enter a number"))
b=int(input("enter a number"))
try:
    res=a/b
    print(res)
except Exception as e:
    print("error occured")