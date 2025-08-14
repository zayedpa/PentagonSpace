import pickle
class Employee:
    def __init__(self,name,age):
        self.ename=name
        self.eage=age
    def disp(self):
        print(self.ename)
        print(self.eage)
f=open("rumaan.txt","rb")
e1=pickle.load(f)
e1.disp()
f.close()