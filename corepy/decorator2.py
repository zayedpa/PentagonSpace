def main():
    a=10
    b=20
    
def outer(ptr):
    print("answer is")
    def inner():
        res=ptr()
        ans=a+b
        print(ans)
    return inner
ref=outer(main)
ref()
