# fibonacci serise
class Fibo:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        a = 0
        b = 1
        while a < self.max:
            yield a
            a, b = b, a+b


x = Fibo(100)
for i in x:
    print(i, end=" ")
print(55 in x, 50 in x)