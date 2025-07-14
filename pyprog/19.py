n=5
for i in range(1,n+1,1):
    x=1
    for j in range(1,n-2+1,1):
        print(x," ",end="")
        x=x+1
    x=2
    for j in range(1,n-3+1,1):
        print(x," ",end="")
        x=x-1
    print("")