import sys
sys.stdin = open('11047.txt', 'r')

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    A = [int(input()) for _ in range(N)]

    x = 0
    for a in range(len(A) - 1, -1, -1):
        if A[a] < K:
            x = a
            break

    val = 0
    cnt = 0
    while val != K:
        if val > K:
            val -= A[x]
            cnt -= 1
            x -= 1
        else:
            val += A[x]
            cnt += 1

    print(cnt)
    # N, K = map(int, input().split())
    # coins = []
    # for _ in range(N):
    #     coins += [int(input())]
    #
    # for coin in coins:
    #     if coin > K:
    #         coins = coins[:coins.index(coin)]
    #         break
    #
    # answer = 0
    # i = -1
    # while K > 0:
    #     coin = coins[i]
    #     if coin <= K:
    #         K -= coin
    #         answer += 1
    #     else:
    #         i -= 1
