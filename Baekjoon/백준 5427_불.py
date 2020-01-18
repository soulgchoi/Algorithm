import sys
sys.stdin = open('5427.txt', 'r')

T = int(input())
for _ in range(T):
    W, H = map(int, input().split())
    data = [list(d for d in input()) for _ in range(H)]
    path = [[0]*W for _ in range(H)]
    dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def solve():
        def gogo(x, y, z):
            if 0 <= x < H and 0 <= y < W:
                if not visited[x][y] and data[x][y] != '*' and data[x][y] != '#':
                    return 1
                else:
                    return -1
            else:
                if z in ['.', '@']:
                    return 0
                else:
                    return -1

        def taeyeon(ls):
            temp = []
            for f, r in ls:
                for df, dr in dxdy:
                    nf, nr = f + df, r + dr
                    if 0 <= nf < H and 0 <= nr < W:
                        if data[nf][nr] in ['.', '@']:
                            data[nf][nr] = '*'
                            temp += [(nf, nr)]
            return temp

        def escape(ls):
            temp = []
            for e, s in ls:
                for de, ds in dxdy:
                    ne, ns = e + de, s + ds
                    go = gogo(ne, ns, data[e][s])
                    if go == 1:
                        path[ne][ns] = path[e][s] + 1
                        temp += [(ne, ns)]
                        visited[ne][ns] = 1
                    elif go == 0:
                        return path[e][s] + 1
            return temp

        fire = []
        for i2 in range(H):
            for j2 in range(W):
                if data[i2][j2] == '*':
                    fire += [(i2, j2)]

        visited = [[0]*W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                if data[i][j] == '@':
                    sanggeun = [(i, j)]
                    visited[i][j] = 1
                    while True:
                        sanggeun = escape(sanggeun)
                        fire = taeyeon(fire)
                        if type(sanggeun) == int:
                            return sanggeun
                        elif not sanggeun:
                            return 'IMPOSSIBLE'

    print(solve())


