def acronymize(xs):
    ys = xs.split(" ")
    a = ""
    for y in ys:
        if y[0].isupper():
            a += y[0]
    return a

print(acronymize("Indian Institute of Technology"))