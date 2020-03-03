import sys
sys.stdin = open('1861.txt', 'r')


def canGo(a, b, c, d):
	if 0 <= c < N and 0 <= d < N:
		if room[c][d] == room[a][b] + 1:
			return 1
		else:
			return 0

T = int(input())
for tc in range(1, T+1):
	N = int(input())
	room = [list(map(int, input().split())) for _ in range(N)]
	dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
	visited = [[0]*N for _ in range(N)]
	ans = (0, 0)
	for i in range(N):
		for j in range(N):
			if visited[i][j]:
				continue
			stack = [(i, j)]
			visited[i][j] = 1
			cnt = 1
			while stack:
				x, y = stack.pop()
				for dx, dy in dxdy:
					nx, ny = x + dx, y + dy
					if canGo(x, y, nx, ny):
						cnt += 1
						stack += [(nx, ny)]
						visited[nx][ny] = 1
						break
			if cnt > ans[1]:
				ans = (room[i][j], cnt)
			elif cnt == ans[1]:
				if room[i][j] < ans[0]:
					ans = (room[i][j], cnt)

	print('#%d %d %d' % (tc, ans[0], ans[1]))




