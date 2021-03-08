def gamble(x):
    from random import choice
    r = choice([0, 1])
    if r == 0:
        return x // 2
    else:
        return x * 2

y = 100
n = 0

while y > 0:
    n += 1
    y = gamble(y)

print(n)