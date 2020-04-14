def fibonacci(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

wynik=fibonacci(20)
for i in range(20):
    print(next(wynik))

