import sys
sys.stdin = open('2573.txt', 'r')


N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
check = [[0]*M for _ in range(N)]

dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
time = 0
flag = False
while data != check:
    visited = [[0]*M for _ in range(N)]
    time += 1
    ice = 0
    for i in range(1, N-1):
        for j in range(1, M-1):
            if data[i][j] != 0 and not visited[i][j]:
                queue = [(i, j)]
                height = []
                visited[i][j] = 1
                front, rear = -1, 0
                while front != rear:
                    front += 1
                    x, y = queue[front]
                    temp = 0
                    for dx, dy in dxdy:
                        nx, ny = x + dx, y + dy
                        if data[nx][ny] == 0:
                            temp += 1
                        elif data[nx][ny] != 0 and not visited[nx][ny]:
                            queue += [(nx, ny)]
                            visited[nx][ny] = 1
                            rear += 1
                    height += [(x, y, data[x][y] - temp)]
                for h1, h2, h3 in height:
                    if h3 <= 0:
                        data[h1][h2] = 0
                    else:
                        data[h1][h2] = h3
                ice += 1
    if ice > 1:
        flag = True
        break

if flag:
    print(time-1)
else:
    print(0)

            

