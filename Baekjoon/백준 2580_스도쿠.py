import sys
sys.stdin = open('2580.txt', 'r')

sudoku = [list(map(int, input().split())) for _ in range(9)]
print(sudoku)

# 0 이라면
# 1~9 중에 들어갈 수 있는거 체크
# 넣어서 다음으로 dfs
# 0으로 초기화
# 다른거 넣어봄
# 81칸 다 차면 끝

