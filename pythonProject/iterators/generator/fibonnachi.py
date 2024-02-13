def fibonacci():
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b

f = fibonacci()
for f in fibonacci():
    if f > 10000:
        break
    print(f)