str=input("enter a string")
print(str)
if str.isalpha():
    print("str contains alphabets" )
elif str.isdigit():
    print("string contains digits")
elif str.isalnum():
    print("str contains both")
else:
    print("str contains other characters")