def is_odd(n):
    return n % 2 == 1

def next(n):
    if is_odd(n):
        return 3*n + 1
    else:
        return n // 2

def test_next():
    assert next(5) == 16
    assert next(16) == 8
    assert next(18) == 9
    assert next(9) == 28