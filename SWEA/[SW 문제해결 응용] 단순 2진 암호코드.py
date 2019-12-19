import sys
sys.stdin = open('[SW 문제해결 응용] 단순 2진 암호코드.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    code = [list(input()) for _ in range(N)]

    print(code)