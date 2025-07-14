class Demo:
    def disp(self,x=10,y=20,z=30):   #default arguments
        print(x)
        print(y)
        print(z)
d1=Demo()
a=11
b=22
c=33
d1.disp()   # output 10,20,30
d1.disp(a,b,c)   # 11,22,33
d1.disp(a)    #11,20,30
d1.disp(c)   #33,20,30
d1.disp(x=b,y=c,z=a)  #22,33,11     keyword arguments
d1.disp(x=c)    #33,20,30
    