class parent:
    def __init__(self):
        self.a=10
class child(parent):
    def __init__(self):
        parent.__init__(self)
        self.b=20
c1=child()
print(c1.b)
print(c1.a)