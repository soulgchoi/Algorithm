# 테케 5개
from copy import deepcopy
import sys
sys.stdin = open('17822.txt', 'r')

# for _ in range(5):
N, M, T = map(int, input().split())
circle = [list(map(int, input().split())) for _ in range(N)]
wheel = [list(map(int, input().split())) for _ in range(T)]



def bing1(ls, cnt):
	temp = [0] * len(ls)
	while cnt > 0:
		for m in range(M):
			temp[(M+m+1) % M] = ls[m]
		ls = temp
		temp = [0] * len(ls)
		cnt -= 1
	return ls

def bing2(ls, cnt):
	temp = [0] * len(ls)
	while cnt > 0:
		for m in range(M):
			temp[m] = ls[(M+m+1) % M]
		ls = temp
		temp = [0] * len(ls)
		cnt -= 1
	return ls
# 위의 과정을 T 번 한다.

# 돌릴 때마다 ( 인접하고, 같은 수이면 ) 지운다.
# circle 에서 각 리스트의 인덱스 0 과 -1(==M-1) 은 인접한다.
# (i, j) 일 떄, i 가 +- 1이고 j 값이 같다 == 인접한다.
# (i, j) 일 때, i 가 같고 j +- 1 == 인접한다.
def rmv(ls):
	dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
	visited = [[0]*M for _ in range(N)]
	for i in range(N):
		for j in range(M):
			if not visited[i][j]:
				visited[i][j] = 1
				val = ls[i][j]
				queue = [(i, j)]
				front, rear = -1, 0
				while front != rear:
					front += 1
					i2, j2 = queue[front]
					for dx, dy in dxdy:
						ni, nj = i2+dx, j2+dy
						if 0 <= ni < N and -1 <= nj < M+1:
							if nj == M:
								nj = 0
							if ls[ni][nj] == val and not visited[ni][nj]:
								ls[ni][nj] = 0
								ls[i][j] = 0
								if nj == -1:
									queue += [(ni, M-1)]
								else:
									queue += [(ni, nj)]
								visited[ni][nj] = 1
								rear += 1
	return ls

def nrmv(ls):
	numbers = 0
	s_nums = 0
	for l in ls:
		s_nums += sum(l)
		numbers += M - l.count(0)
	avg = s_nums / numbers
	for n in range(N):
		for m in range(M):
			if ls[n][m] != 0:
				if ls[n][m] > avg:
					ls[n][m] -= 1
				elif ls[n][m] < avg:
					ls[n][m] += 1
	return ls



# 돌릴 원판을 찾는다.

for t in range(T):  # T 번
	X, D, K = wheel[t]
	for n in range(N):  # 원판에서
		if not (n+1) % X:  # x 의 배수이면
			target = circle[n]  # 돌릴 원판
			# print(target)
			if D:  # 반시계 방향
				target = bing2(target, K)
				circle[n] = target
			else:  # 시계 방향
				target = bing1(target, K)
				circle[n] = target
	# 여기서 인접한 수를 지운다.
	check = deepcopy(circle)
	circle = rmv(circle)
	# 인접한 수가 없으면 원판에 적힌 수의 평균을 구하고,
	# 평균보다 큰 수는 -1, 작은 수는 +1 한다.
	if circle == check:
		circle = nrmv(circle)

print(sum(sum(c) for c in circle))

