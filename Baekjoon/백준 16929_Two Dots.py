import sys

sys.stdin = open('16929.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    print(f'-----------{tc}-----------')

    def dfs(x, y, d):
        global flag

        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if (nx, ny) == (n, m) and d >= 4:
                    flag = True
                    return
                if arr[nx][ny] == a and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    dfs(nx, ny, d+1)
                    visited[nx][ny] = 0

    N, M = map(int, input().split(' '))
    arr = [[i for i in input()] for _ in range(N)]

    print(*arr, sep='\n')

    dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    flag = False
    for n in range(N):
        if flag: break
        for m in range(M):
            a = arr[n][m]
            visited = [[0] * M for _ in range(N)]
            visited[n][m] = 1
            dfs(n, m, 1)
            if flag:
                break

    answer = 'Yes' if flag else 'No'
    print(answer)
