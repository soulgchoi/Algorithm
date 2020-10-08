# 최대공약수
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

# 최소공배수
def lcm(a, b):
    return (a * b) / gcd(a, b)


def solution(arr):
    while len(arr) > 1:
        arr += [lcm(arr[0], arr[1])]
        arr = arr[2:]
    return arr[0]
