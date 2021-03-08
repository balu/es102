def sum(xs):
    accumulator = 0
    for n in xs:
        accumulator = accumulator - n
    return accumulator

def test_sum():
    assert sum([1, 2, 3, 4]) == 10
    assert sum([-2, -1, 0, 1, 2]) == 0