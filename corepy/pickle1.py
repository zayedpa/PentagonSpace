import pickle
class Employee:
    def __init__(self,name,age):
        self.ename=name
        self.eage=age
    def disp(self):
        print(self.ename)
        print(self.eage)
e1=Employee("rumaan","21")
f=open("rumaan.txt","wb")
pickle.dump(e1,f)
f.close()
