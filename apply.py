def apply(f, x):
    return f(x)

def inc(x):
    return x+1

def dec(x):
    return x-1

print(apply(inc, 3))
print(apply(dec, 9))

def apply_twice(f, x):
    return f(f(x))

print(apply_twice(inc, 3))

def apply_n(f, n, x):
    y = x
    while n > 0:
        y = f(y)
        n -= 1
    return y

print(apply_n(inc, 100, 3))

def apply_all(fs, x):
    y = x
    for f in fs:
        y = f(y)
    return y

print(apply_all([inc, inc, dec, inc, dec, dec, dec, dec], 9))