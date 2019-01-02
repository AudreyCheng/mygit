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

s = 0


def fac_sum(n):
    for i in range(1, n+1):
        s = s + fac(i)
        return s

print fac(4)
# print fac_sum(4)





# def n_factorial(n):
#     result = 1
#     i = 1
#     for i in range(n):
#         i = i+1
#         result = i*(i+1)
#         return result
#
# print n_factorial(4)