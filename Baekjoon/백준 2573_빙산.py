import sys
sys.stdin = open('2573.txt', 'r')


def ice():  # 빙산 분리되는지 체크
    global height, dxdy
    cnt = 0
    visited = [[0]*M for _ in range(N)]
    for s, t, r in height:
        stack = [(s, t)]
        while stack:
            a, b = stack.pop()
            if not visited[a][b]:
                visited[a][b] = 1
                for da, db in dxdy:
                    na, nb = a + da, b + db
                    if 0 <= na < N and 0 <= nb < M:
                        if not visited[na][nb]:
                            if data[na][nb] != 0:
                                stack += [(na, nb)]
                            visited[na][nb] = 1
        cnt += 1
    return cnt


N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

height = []
for i in range(N):
    for j in range(M):
        if data[i][j]:
            height += [(i, j, 0)]

dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

time = 0
peng = 0
while peng <= 2:
    time += 1
    for k in range(len(height)):
        x, y, h = height[k]
        temp = 0
        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if data[nx][ny] == 0:
                    temp += 1
        height[k] = x, y, h-temp
    for x2, y2, h2 in height:
        if h2 <= 0:
            data[x2][y2] = 0
        else:
            data[x2][y2] = h2
    peng = ice()

print(time)
