def root_of_quadratic(a, b, c):
    from math import sqrt
    discriminant = b * b - 4 * a * c
    return (-b + sqrt(discriminant)) / (2 * a)

r = root_of_quadratic(1, 5, 3)
print(r)
print(r*r + 5*r + 3)