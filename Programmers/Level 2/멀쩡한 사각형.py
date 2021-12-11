def greatestCommonDivisor(a, b):
    return a if b == 0 else greatestCommonDivisor(b, a % b)


def solution(w, h):
    gcd = greatestCommonDivisor(w, h)
    return (w * h) - ((w / gcd) + (h / gcd) - 1) * gcd
