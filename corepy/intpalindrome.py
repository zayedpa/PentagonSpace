num=int(input("enter a number"))
original_number=num
rev=0
i=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
if rev==original_number:
    print("palindrome")
else:
    print("not palindrome")

