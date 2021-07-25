import sys
sys.stdin = open('9322.txt', 'r')

T = int(input())
for _ in range(T):
    ls = int(input())

    key1 = list(input().split(' '))
    key2 = list(input().split(' '))

    e = list(input().split(' '))

    rule = [key1.index(k) for k in key2]

    ans = list(range(len(e)))
    for i in range(len(e)):
        ans[rule[i]] = e[i]

    print(' '.join(ans))
