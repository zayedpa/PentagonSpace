def generator():
    yield 1
    yield 2
    yield 3
res=generator()
print(res)
print(next(res))
print(next(res))
print(next(res))