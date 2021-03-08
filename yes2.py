def yes(n, i=0):
    if i < n:
        print('y')
        yes(n, i+1)

yes(5)
