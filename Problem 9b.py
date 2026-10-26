n = int(input())

for a in range(2 * n, n, -1):
    b = a * n / (a - n)
    if b.is_integer() and b > a:
        print(a, int(b))
        exit()