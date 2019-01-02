def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)

    while True:
        a = int(input(a))
        if a < 0:
            break
        else:
            print fac(a)
print fac(4)
