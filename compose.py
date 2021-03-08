def square(x):
    return x*x

def cube(x):
    return x*x*x

def compose(f, g):
    def h(x):
        return f(g(x))
    return h

def test_compose():
    sixth = compose(square, cube)
    assert sixth(2) == 64

def greeter(s):
    def greet(name):
        return f"{s}, {name}."
    return greet

hello = greeter("Hello")
print(hello("Joe"))

hi = greeter("Hi")
print(hi("Joe"))