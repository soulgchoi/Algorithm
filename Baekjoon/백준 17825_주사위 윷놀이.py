# 테케 4개

import sys
sys.stdin = open('17825.txt', 'r')

dice = list(map(int, input().split()))

print(dice)

# 말은 네 개이다.

# 각 칸의 값이 점수로 추가된다.
# 화살표 방향대로 이동한다.
# 10, 20, 30 에서 파란 화살표
# 10, 20, 30 을 제외한 짝수는 모두 한 칸이다.
# 10 이면 13, 16, 19, 25, 30, 35, 40
# 20 이면 22, 24, 25, 30, ..
# 30 이면 28, 27, 26, 25
# 25이면 무조건 30, 35, 40, 도착
# 외에는 2, 4, ... , 40 (10, 20, 30 제외)

game = list(range(41))
print(game)
tf = [25, 30, 35, 40]
blue1 = [10, 13, 16, 19]
blue2 = [20, 22, 24]
blue3 = [30, 28, 27, 26]
for g in range(41):
    if g % 2 and g not in (tf + blue1 + blue2 + blue3):
        game[g] = 0
# 위의 윷놀이 판에서 0 보다 클 때만 주사위 숫자를 - 한다.

# 말은 항상 점수와 위치를 저장한다.
# depth 로 10번 채우면 return 한다.
# 가장 큰 값을 찾는다.
# [0, 0, 0, 0]
# 말 네개를 1, 0 초기화하며 들어간다.
# 작으면 안간다.

mal = [0, 0, 0, 0]
ans = 0

def solve(k, val):
    global ans, mal, game, dice
    if k == 10:
        if val > ans:
            ans = val
            return
    else:
        for i in range(4):
            dk = dice[k]
            g = 0
            while dk > 0:
                if game[g] == 0:
                    g += 1
                else:
                    if game[g] == 10:
                        