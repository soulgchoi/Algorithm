import sys
sys.stdin = open('[S/W 문제해결 응용] 최적 경로.txt', 'r')

def perm(arr, k, N):
    if k == N:
        home(arr)
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm(arr, k+1, N)
            arr[k], arr[i] = arr[i], arr[k]

def home(arr):
    global ans
    arr = [0] + arr + [N + 1]

    path = 0
    x = 0
    for s in range(N + 1):
        if ans > path:
            path += n[arr[s]][arr[s+1]]
        else:
            break

    if ans > path:
        ans = path


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    m = [data[i:i + 2] for i in range(0, (N + 2) * 2, 2)]
    m2 = m.pop(1)
    m.append(m2)
    n = [[0] * (N + 2) for _ in range(N + 2)]

    customer = [n for n in range(1, N + 1)]
    print(customer)
    ans = 9999

    for i in range(N+2):
        for j in range(N+2):
            n[i][j] = abs(m[i][0]-m[j][0]) + abs(m[i][1]-m[j][1])

    # permute(customer)
    perm(customer, 0, N)
    print('#%d %d' % (tc, ans))