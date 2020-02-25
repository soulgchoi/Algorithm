import sys
sys.stdin = open('17825.txt', 'r')

dice = list(map(int, input().split()))
mal = [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]]
ans = 0

boardRed = list(range(0, 39, 2))
boardBlueOne = [10, 13, 16, 19]
boardBlueTwo = [20, 22, 24]
boardBlueThree = [30, 28, 27, 26]
boardExtra = [25, 30, 35, 40]
board = [boardRed, boardBlueOne, boardBlueTwo, boardBlueThree, boardExtra]

visited = [
    [0]*len(boardRed),
    [0]*len(boardBlueOne),
    [0]*len(boardBlueTwo),
    [0]*len(boardBlueThree),
    [0]*len(boardExtra)
]

def isBlue(x, y):
    if board[mal[x][0]][mal[x][1]] == 10:
        mal[x] = [1, 0, y]
    elif board[mal[x][0]][mal[x][1]] == 20:
        mal[x] = [2, 0, y]
    elif mal[x][0] == 0 and board[mal[x][0]][mal[x][1]] == 30:
        mal[x] = [3, 0, y]

def solve(k, val):
    global ans, visited
    if k == 10:
        ans = max(val, ans)
    else:
        for i in range(4):
            if mal[i][2]:
                isBlue(i, mal[i][2])
                a, b, c = mal[i]
                if b + dice[k] > len(board[a])-1:
                    if a == 4:
                        # visited[a][b] = 0
                        # mal[i][2] = 0
                        # solve(k+1, val)
                        # visited[a][b] = 1
                        # mal[i][2] = 1
                        continue
                    else:
                        temp = dice[k] - (len(board[a])-b)
                        if temp > len(board[4])-1:
                            # visited[a][b] = 0
                            # mal[i][2] = 0
                            # solve(k + 1, val)
                            # visited[a][b] = 1
                            # mal[i][2] = 1
                            continue
                        else:
                            if not visited[4][temp]:
                                visited[a][b] = 0
                                mal[i] = [4, temp, 1]
                                visited[4][temp] = 1
                                solve(k + 1, val + board[4][temp])
                                visited[a][b] = 1
                                visited[4][temp] = 0
                                mal[i] = [a, b, c]
                else:
                    if not visited[a][b+dice[k]]:
                        visited[a][b] = 0
                        mal[i] = [a, b + dice[k], 1]
                        isBlue(i, mal[i][2])
                        visited[mal[i][0]][mal[i][1]] = 1
                        solve(k+1, val+board[mal[i][0]][mal[i][1]])
                        visited[a][b] = 1
                        visited[mal[i][0]][mal[i][1]] = 0
                        mal[i] = [a, b, c]

solve(0, 0)
print(ans)