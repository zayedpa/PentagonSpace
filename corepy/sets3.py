a=set()
for i in range(5):
    data=int(input("Enter a num"))
    a.add(data)
print(a)

a.update([60,70,80])
print(a)

a.discard(80)
print(a)