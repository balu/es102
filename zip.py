def zip(xs, ys):
    zs = []
    i  = 0
    while i < len(xs):
        zs.append((xs[i], ys[i]))
        i += 1
    return zs

print(zip([1, 2], [3, 4]))