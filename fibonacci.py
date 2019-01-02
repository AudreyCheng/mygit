def fibonacci(n):
    f_list = [1, 1]
    if 2 >= n > 0:
        return f_list[0:n]
    for i in range(2, n):
        f_list.append(f_list[-1] + f_list[-2])

    return f_list

f_list = fibonacci(8)
print f_list




