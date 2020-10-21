import math

def solution(n,a,b):
    m = int(math.log2(n))
    while True:
        x = range(1, n//2+1)
        y = range(n//2+1, n+1)
        if a in x and b in x:
            n //= 2
            m -= 1
        elif a in y and b in y:
            n //= 2
            a, b = a - n, b - n
            m -= 1
        else:
            return m
