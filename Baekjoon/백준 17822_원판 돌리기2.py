from copy import deepcopy
import sys
sys.stdin = open('17822.txt','r')


def bing1(ls, cnt):
	temp = [0] * len(ls)
	for _ in range(cnt):
		for m in range(M):
			temp[(M+m+1) % M] = ls[m]
		ls = temp
		temp = [0] * len(ls)
	return ls

def bing2(ls, cnt):
	temp = [0] * len(ls)
	for _ in range(cnt):
		for m in range(M):
			temp[m] = ls[(M+m+1) % M]
		ls = temp
		temp = [0] * len(ls)
	return ls

def rmv(ls):
	dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
	visited = [[0]*M for _ in range(N)]
	for i in range(N):
		for j in range(M):
			if not visited[i][j]:
				val = ls[i][j]
				queue = [(i, j)]
				front, rear = -1, 0
				while front != rear:
					front += 1
					i2, j2 = queue[front]
					visited[i2][j2] = 1
					for dx, dy in dxdy:
						ni, nj = i2+dx, j2+dy
						if 0 <= ni < N and -1 <= nj < M+1:
							if nj == M:
								nj = 0
							if nj == -1:
								nj = M-1
							if ls[ni][nj] == val and not visited[ni][nj]:
								ls[ni][nj] = 0
								ls[i][j] = 0
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
	if numbers == 0:
		return ls
	else:
		avg = s_nums / numbers
	for n in range(N):
		for m in range(M):
			if ls[n][m] != 0:
				if ls[n][m] > avg:
					ls[n][m] -= 1
				elif ls[n][m] < avg:
					ls[n][m] += 1
	return ls


N, M, T = map(int, input().split())
circle = [list(map(int, input().split())) for _ in range(N)]
wheel = [list(map(int, input().split())) for _ in range(T)]

for t in range(T):
	X, D, K = wheel[t]
	for n in range(N):
		if not (n+1) % X:
			target = circle[n]
			if D:
				target = bing2(target, K)
				circle[n] = target
			else:
				target = bing1(target, K)
				circle[n] = target
	check = deepcopy(circle)
	circle = rmv(circle)
	if circle == check:
		circle = nrmv(circle)

print(sum(sum(c) for c in circle))