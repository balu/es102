def square(xs):
    ys = []
    for x in xs:
        ys.append(x*x)
    return ys

def test_square():
    assert square([]) == []
    assert square([1, 2, 3]) == [1, 4, 9]

def filter_positive(xs):
    ys = []
    for x in xs:
        if x > 0:
            ys.append(x)
    return ys

def test_filter_positive():
    assert filter_positive([-1, -2, -3]) == []
    assert filter_positive([-1, 0, 1, -1, 2]) == [1, 2]