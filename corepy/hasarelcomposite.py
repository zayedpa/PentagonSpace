class os:
    def  __init__(self):
        self.status=True
        print("os is ready")
    def getos(self):
        print("os is installing")
class mobile:
    def __init__(self,name):
        self.mname=name
        self.o=os()
        print("mobile is ready")
        print("with os is installed")
m1=mobile("vivo")
print(m1.mname)
print(m1.o.status)
m1.o.getos()
# del m1
# print(m1.o.status)
# this is a composite function without main object m1,os cant exist