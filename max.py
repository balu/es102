def max(xs):
    maximum = -10000
    for x in xs:
        if x > maximum:
            maximum = x
    return maximum

def test_max():
    assert max([]) == -10000
    assert max([1, -4, 5, 9, 3]) == 9
    assert max([-100]) == -100