import sys
sys.stdin = open('2573.txt', 'r')


# def ice():  # 빙산 분리되는지 체크
#     global height, dxdy
#     cnt = 0
#     visited = [[0]*M for _ in range(N)]
#     for s, t, r in height:
#         if not visited[s][t] and data[s][t] != 0:
#             stack = [(s, t)]
#             a, b = stack[-1]
#             while stack:
#                 visited[a][b] = 1
#                 for da, db in dxdy:
#                     na, nb = a + da, b + db
#                     if 0 <= na < N and 0 <= nb < M:
#                         if not visited[na][nb]:
#                             if data[na][nb] != 0:
#                                 stack += [(na, nb)]
#                                 a, b = na, nb
#                                 # visited[na][nb] = 1
#                                 break
#             cnt += 1
#     return cnt


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
while peng < 2:
    visited = [[0] * M for _ in range(N)]
    for k in range(len(height)):
        x, y, h = height[k]
        if h != 0 and not visited[x][y]:
            queue = [(x, y)]
            front, rear = -1, 0
            while front != rear:
                front += 1
                x, y = queue[front]
                temp = 0
                for dx, dy in dxdy:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M:
                        if data[nx][ny] == 0:
                            temp += 1
                            queue += [(nx, ny)]
                            visited[nx][ny] = 1
                height[k] = x, y, data[x][y]-temp
            peng += 1
    for k2 in range(len(height)):
        x2, y2, h2 = height[k2]
        if h2 <= 0:
            data[x2][y2] = 0
        else:
            data[x2][y2] = h2
    time += 1

if peng >= 2:
    print(time)
else:
    print(0)
