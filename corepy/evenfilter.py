def even(num):
    if num%2==0:
        return True
    else:
        return False
l=[1,2,3,4,5]
res=list(filter(even,l))
print(res)