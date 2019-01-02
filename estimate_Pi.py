import random
import math


class Point(object):

    def __init__(self, x, y):
         self.x = x
         self.y = y

    def get_distance(self):
        return math.sqrt((self.x-1)**2+(self.y-1)**2)


def monte_carlo(n):
    in_circle = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        p = Point(x, y)
        d = p.get_distance()
        if d <= 1.0:
            in_circle = in_circle + 1
    pi = 4.0 * in_circle / n
    return pi

print monte_carlo(10000)

