class A:
    def disp(self):
        print("A")
class B(A):
    def disp(self):
        print("B")
class C(B):
    def disp(self):
        print("C")
        B.disp(self)
        A.disp(self)

c1=C()
c1.disp()
