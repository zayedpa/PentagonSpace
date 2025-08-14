ptr=open("car.jpg","rb")
data=ptr.read(50000)
print(data)
ptr.close()

ptr1=open("newcar.jpg","wb")
ptr1.write(data)
ptr1.close()