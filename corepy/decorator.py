def main():
    print("unside main")
def outer(ptr):
        print("inside outer")
        def inner():
            print("entering inner")
            ptr1=ptr
            ptr()
            print("leaving inner")
        return inner
ref=outer(main)
ref()