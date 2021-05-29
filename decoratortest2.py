def my_decorator(fn):
    def wrapper():
        print("hi...... starting execution")
        fn()
        print("Bye..... finished execution")
    return wrapper

def func1():
    print("Hello world")
    print("Welcome to python")

def func2():
    for i in range(10):
        print(i, end=" ")
    print()

@my_decorator
def func3():
    print("Learning Decorators")
func1 = my_decorator(func1)
func2 = my_decorator(func2)
func1()
print()
func2()
print()
func3()
