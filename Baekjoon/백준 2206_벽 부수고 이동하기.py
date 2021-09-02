import sys
from collections import deque

sys.stdin = open('2206.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    print(f'------------{tc}-------------')

    N, M = map(int, input().split(' '))
    array = [list(map(int, input())) for _ in range(N)]

    dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]  # 벽을 부쉈는지 안부쉈는지도 함께 기록할 3중 포문

    queue = deque()
    queue.append((0, 0, 0))  # x, y, 벽
    visited[0][0][0] = 1
    front, rear = -1, 0
    answer = 0
    while front < rear:
        front += 1
        x, y, w = queue[front]
        if (x, y) == (N-1, M-1):  # 목적지에 도달하면 break
            answer = visited[x][y][w]
            break
        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny][w]:
                if array[x][y] == 1 and w == 0:  # 벽인데 부술 수 있을 때
                    queue.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][w] + 1
                    rear += 1
                if array[x][y] == 0:
                    queue.append((nx, ny, w))
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    rear += 1
    answer = answer if answer else -1
    print(answer)


# def dfs(x, y, v, w, d):
#     global answer
#     if (x, y) == (N, M):
#         if d < answer:
#             answer = d
#         return
#
#     for dx, dy in dxdy:
#         nx, ny = x + dx, y + dy
#         if 0 <= nx <= N and 0 <= ny <= M and not v[nx][ny]:
#             if array[nx][ny] and w:
#                 v[nx][ny] = 1
#                 dfs(nx, ny, v, w - 1, d + 1)
#                 v[nx][ny] = 0
#             if array[nx][ny] == 0:
#                 v[nx][ny] = 1
#                 dfs(nx, ny, v, w, d + 1)
#                 v[nx][ny] = 0
#
#
# N, M = map(int, input().split(' '))
# array = [list(map(int, input())) for _ in range(N)]
#
# answer = 999999
# dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# visited = [[0] * M for _ in range(N)]
# visited[0][0] = 1
#
# N, M = N - 1, M - 1
# dfs(0, 0, visited, 1, 1)
#
# if answer == 999999:
#     answer = -1
# print(answer)
