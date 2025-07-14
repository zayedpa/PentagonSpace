class A:
    def disp(self):
        print("A")
class B(A):
    def disp(self):
        print("B")
class C(B):
    def disp(self):
        print("C")

c1=C()
c1.disp()
c1.disp()
c1.disp()