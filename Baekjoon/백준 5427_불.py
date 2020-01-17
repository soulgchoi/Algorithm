import sys
sys.stdin = open('5427.txt', 'r')

T = int(input())
for _ in range(T):
    W, H = map(int, input().split())
    data = [list(d for d in input()) for _ in range(H)]
    path = [[0]*W for _ in range(H)]
    dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    """
        . 빈 공간
        # 벽
        @ 상근이 위치
        * 불
    """

    def solve():
        def gogo(x, y, z):
            if 0 <= x < H and 0 <= y < W:
                if not visited[x][y] and data[x][y] != '*' and data[x][y] != '#':
                    return 1
                else:
                    return -1
            else:
                if z == '.':
                    return 0
                else:
                    return -1

        def taeyeon(ls):
            temp = []
            for f, r in ls:
                for df, dr in dxdy:
                    nf, nr = f + df, r + dr
                    if 0 <= nf < H and 0 <= nr < W:
                        if data[nf][nr] == '.':
                            data[nf][nr] = '*'
                            temp += [(nf, nr)]
            return ls + temp

        fire = []
        for k in range(H):
            for l in range(W):
                if data[k][l] == '*':
                    fire += [(k, l)]

        visited = [[0]*W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                if data[i][j] == '@':
                    queue = [(i, j)]
                    visited[i][j] = 1
                    front, rear = -1, 0
                    while front != rear:
                        front += 1
                        x, y = queue[front]
                        fire = taeyeon(fire)
                        for dx, dy in dxdy:
                            nx, ny = x + dx, y + dy
                            go = gogo(nx, ny, data[x][y])
                            if go == 1:
                                path[nx][ny] = path[x][y] + 1
                                queue += [(nx, ny)]
                                visited[nx][ny] = 1
                                rear += 1
                            elif go == 0:
                                return path[x][y] + 1

                    return 'IMPOSSIBLE'


    print(solve())


