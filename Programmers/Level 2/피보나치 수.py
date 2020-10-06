# 처음에 재귀로 풀었는데 이게 훨씬 빨랐다.
def solution(n):
    fibo = [0 for _ in range(n+1)]
    fibo[1] = 1
    for i in range(2, n+1):
        fibo[i] = fibo[i-2] + fibo[i-1]
    return fibo[n] % 1234567


# 재귀 코드
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n - 2) + fibo(n - 1)

def solution(n):
    return fibo(n) % 1234567