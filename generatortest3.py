def fibo():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a+b

fib = fibo()

for i in fib:
    if i > 500:
        break
    print(i, end=" ")