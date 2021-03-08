def first_negative(xs):
    for x in xs:
        if x < 0:
            return x
    return 0

def test_first_negative():
    assert first_negative([0, 1, 2, -5, -9, 3]) == -5
    assert first_negative([]) == 0
    assert first_negative([1, 2, 3]) == 0
    assert first_negative([-1, 3, 4, 5]) == -1
