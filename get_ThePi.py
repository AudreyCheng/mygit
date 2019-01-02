import random

def get_pi(n):
    inner = 0.0

    for i in range(n) :
        x = random.random()
        y = random.random()

        if x ** 2 + y ** 2 <= 1 :
            inner += 1

    pi = 4 * inner / n
    return pi

print get_pi(1000)