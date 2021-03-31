# Syntax Sugar

def maximum(x, y):
    if x > y:
        m = x
    else:
        m = y
    return m

print(maximum(4, 5))
print(maximum(5, 4))
print(maximum(5, 5))

# if else expressions
def maximum(x, y):
    return x if x > y else y

print(maximum(4, 5))
print(maximum(5, 4))
print(maximum(5, 5))

def square(x):
    return x*x

def maplist(f, xs):
    ys = []
    for x in xs:
        ys.append(f(x))
    return ys

print(maplist(square, [1, 2, 3, 4]))

# lambda expressions
print(maplist(lambda x: x*x, [1, 2, 3, 4]))
print(maplist(lambda x: x*x*x, [1, 2, 3, 4]))

# long form list comprehension
xs = []
for x in [1, 2, 3, 4]:
    xs.append(x*x)
print(xs)

# list comprehensions
print([x*x for x in [1, 2, 3, 4]])
print([x*x*x for x in [1, 2, 3, 4]])

xs = []
for x in [1, 2, 3, 4]:
    for y in [1, 2, 3]:
        xs.append(x*y)
print(xs)

print([x*y for x in [1, 2, 3, 4] for y in [1, 2, 3]])

from math import sqrt

xs = []
for x in [1, 2, -3, 4, -6, 7]:
    if x >= 0:
        xs.append(sqrt(x))
print(xs)

print([sqrt(x) for x in [1, 2, -3, 4, -6, 7] if x >= 0])