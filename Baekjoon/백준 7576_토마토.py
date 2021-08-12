import sys
from collections import deque

sys.stdin = open('7576.txt', 'r')

T = int(input())
for tc in range(T):
    M, N = map(int, input().split(' '))
    array = [list(map(int, input().split())) for _ in range(N)]

    dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    queue = deque([])
    for r in range(N):
        for c in range(M):
            if array[r][c] == 1:
                queue.append((r, c))

    while queue:
        x, y = queue.popleft()
        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and array[nx][ny] == 0:
                array[nx][ny] = array[x][y] + 1
                queue.append((nx, ny))

    flag = True
    for x in range(N):
        for y in range(M):
            if array[x][y] == 0:
                flag = False

    answer = max(sum(array, [])) - 1 if flag else -1
    print(answer)






