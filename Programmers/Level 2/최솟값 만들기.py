def solution(A,B):
    answer = 0

    a = sorted(A)
    b = sorted(B, reverse=True)
    while a and b:
        answer += (a.pop() * b.pop())

    return answer

# 짧고 좋다!
def solution(A,B):
    a = sorted(A)
    b = sorted(B, reverse=True)
    return sum(i*j for i, j in zip(a, b))