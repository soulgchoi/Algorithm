import sys
sys.stdin = open('2636.txt', 'r')

t = int(input())
for _ in range(t):
    col, row = list(map(int, input().split()))
    cheese = [list(map(int, input().split())) for _ in range(col)]
    s = [[0] * row for _ in range(col)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    ans = 0
    queue = []
    count = 0
    while cheese != s:
        v = [[0] * row for _ in range(col)]
        ans = 0
        queue = [(0, 0)]
        v[0][0] = 1
        front, rear = -1, 0
        while front != rear:
            front += 1
            x, y = queue[front]
            for n in range(4):
                nx = x + dx[n]
                ny = y + dy[n]
                if 0 <= nx < col and 0 <= ny < row and not v[nx][ny]:
                    if cheese[nx][ny]:
                        v[nx][ny] = 1
                        cheese[nx][ny] = 0
                        ans += 1
                    else:
                        queue += [(nx, ny)]
                        v[nx][ny] = 1
                        rear += 1
        count += 1

    print(count)
    print(ans)