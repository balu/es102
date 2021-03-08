def is_odd(n):
    return n % 2 == 1

def collatz(n):
    xs = []
    while n != 1:
        xs.append(n)
        if is_odd(n):
            n = 3*n + 1
        else:
            n = n // 2
    xs.append(1)
    return xs

def test_collatz():
    assert collatz(8) == [8, 4, 2, 1]
    assert collatz(5) == [5, 16, 8, 4, 2, 1]
