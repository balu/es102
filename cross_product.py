def cross_product(xs, ys):
    zs = []
    for x in xs:
        for y in ys:
            zs.append((x, y))
    return zs

def test_cross_product():
    assert cross_product([2, 3], [5, 7]) == [(2, 5), (2, 7), (3, 5), (3, 7)]
    assert cross_product([], [1, 2]) == []