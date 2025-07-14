def main():
    str='pentagon'
    return str
def outer(ptr):
        print("inside outer")
        def inner():
            print('inside inner')
            res=ptr()
            ans=res.upper()
            print(ans)
        return inner
ref=outer(main)
ref()