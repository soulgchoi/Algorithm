import sys
sys.stdin = open('6190.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    result = []
    for i in range(N):
        b1 = A[i]
        for j in range(N):
            if j != i:
                b2 = A[j]

                X = str(b1*b2)
                check = 1
                if len(X) >= 2:
                    x = 0
                    while x < len(X) - 1:
                        if X[x] <= X[x + 1]:
                            x += 1
                        else:
                            x += 1
                            check = 0
                if check:
                    result.append(b1 * b2)

    if len(result) >= 1:
        print('#%d %d' % (tc, max(result)))
    else:
        print('#%d %d' % (tc, -1))