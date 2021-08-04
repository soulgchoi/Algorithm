import sys

sys.stdin = open('1543.txt', 'r')

T = int(input())
for _ in range(1, T + 1):
    ans = 0

    s = input()
    t = input()

    ls = len(s)
    lt = len(t)

    i = 0
    while i < ls - lt + 1:
        tmp = s[i:i + lt]
        if tmp == t:
            ans += 1
            i += lt
        else:
            i += 1

    print(ans)
