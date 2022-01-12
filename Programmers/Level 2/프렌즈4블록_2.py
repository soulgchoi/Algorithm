def solution(m, n, board):
    for i in range(m):
        board[i] = list(j for j in board[i])

    dxdy = [(0, 1), (1, 0), (1, 1)]

    while True:
        flag = True
        for r in range(m):
            for c in range(n):
                if board[r][c] == 0: continue
                x, y = r, c
                checked = []
                for dx, dy in dxdy:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if board[nx][ny] == 0: continue
                        if board[nx][ny].lower() == board[x][y].lower():
                            checked += [(nx, ny)]
                if len(checked) == 3:
                    flag = False
                    board[x][y] = board[x][y].lower()
                    for a, b in checked:
                        board[a][b] = board[a][b].lower()
        if flag:
            break

        for r in range(m - 1, -1, -1):
            for c in range(n):
                start, end = r, r
                while end > 0 and (board[end][c] == 0 or board[end][c].islower()):
                    end -= 1
                board[start][c] = board[end][c]
                if board[start][c] != 0 and board[start][c].islower():
                    board[start][c] = 0
                for i in range(start - 1, end - 1, - 1):
                    board[i][c] = 0

    return sum(board, []).count(0)


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))  # 14
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))  # 15
print(solution(6, 6, ["IIIIOO", "IIIOOO", "IIIOOI", "IOOIII", "OOOIII", "OOIIII"]))  # 32
print(solution(6, 2, ["AA", "AA", "CC", "AA", "AA", "DD"]))  # 8
print(solution(8, 2, ["FF", "AA", "CC", "AA", "AA", "CC", "DD", "FF"]))  # 8
print(solution(6, 2, ["DD", "CC", "AA", "AA", "CC", "DD"]))  # 12
print(solution(4, 2, ["CC", "AA", "AA", "CC"]))  # 8
print(solution(3, 2, ["AA", "AA", "AB"]))  # 4
print(solution(2, 2, ["AA", "AB"]))  # 0
print(solution(2, 2, ["AA", "AA"]))  # 4
