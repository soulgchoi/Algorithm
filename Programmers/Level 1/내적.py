def solution(a, b):
    return sum(map(lambda i: a[i] * b[i], range(len(a))))