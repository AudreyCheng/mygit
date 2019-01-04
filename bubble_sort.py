array = [9, 1, 5, 3, 2, 8, 0, 7]


def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

bubble_sort(array)
print array


