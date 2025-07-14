def even(num):
    if num%2==0:
        return True
    else:
        return False
    
l=[1,2,3,4,5]
i=0
while i<=4:
    data=l[i]
    choice=even(data)
    if choice==True:
        print(l[i])
    i=i+1

