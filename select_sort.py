L = [9, 1, 5, 3, 2, 8, 0, 7]


def select_sort(L):
    assert (type(L) == type(['']))
    length = len(L)
    if length <= 1:
        return L

    def _max(s):
        largest = s
        for i in range(s,length):
            if L[i] > L[largest]:
                largest = i
        return largest

    for i in range(length):
        largest = _max(i)
        if i != largest:
            L[i], L[largest] = L[largest], L[i]

    return L

print select_sort(L)