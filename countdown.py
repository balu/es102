def countdown(n):
    from time import sleep
    assert n >= 0
    while n >= 0:
        print(n)
        n = n - 1
        sleep(1)

countdown(-10)