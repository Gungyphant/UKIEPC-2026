import itertools
import math

n = int(input())

for ab_sum in itertools.count():
    for a in range(1, math.ceil(ab_sum / 2)):  # since a and b are interchangeable, a < b must be true
        b = ab_sum - a
        if n * ab_sum == a * b:
            print(a, b)
            exit()
