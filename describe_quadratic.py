def describe_roots(a, b, c):
    discriminant = b*b - 4*a*c
    if discriminant == 0:
        return "A unique real root."
    elif discriminant > 0:
        return "Two real roots."
    else:
        return "Two complex roots."

print(describe_roots(1, 5, 3))
print(describe_roots(1, 3, 3))
print(describe_roots(1, 4, 4))