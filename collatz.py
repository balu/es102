def is_odd(n):
    return n % 2 == 1

def collatz(n):
    while n != 1:
        print(n)
        if is_odd(n):
            n = 3*n + 1
        else:
            n = n // 2
    print(n)

collatz(1005)
