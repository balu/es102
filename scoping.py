x = 1

def f1():
    x = 2

f1()
print(x)

def f(x):
    print(x)

f(2)
print(x)

def g(x):
    print(x)
    x = 3
    def h():
        x = 4
        print(x)
    h()
    def k():
        print(x)
    k()
    print(x)

g(5)
print(x)