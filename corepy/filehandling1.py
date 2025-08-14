#name=input("enter a name")
#ptr=open("rumaan.txt","w")
#ptr.write(name)
#ptr.close()

#name=input("enter a name")
#ptr=open("rumaan.txt","a")
#ptr.write(name)
#ptr.close()

#ptr1=open("rumaan.txt","r")
#res=ptr1.read()
#print(res)
#ptr1.close()


#ptr1=open("rumaan.txt","r")
#res=ptr1.read(4)
#print(res)
#ptr1.close()

#ptr1=open("rumaan.txt","r")
#res=ptr1.readline()
#print(res)
#ptr1.close()

#ptr1=open("rumaan.txt","r")
#res=ptr1.readlines()
#print(res)
#ptr1.close()

ptr=open("rumaan.txt","r")
#res=ptr.tell()
#print(res)
#ptr.close()
data=ptr.read(5)
#print(data)
res1=ptr.tell()
print(res1)

var=ptr.seek(0)
print(var)

res2=ptr.tell()
print(res2)

ptr.close()



