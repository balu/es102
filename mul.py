def mul(x, y):
    product = 0
    while y > 0:
        product += x
        y -= 1
    return product

print(mul(5, 3))