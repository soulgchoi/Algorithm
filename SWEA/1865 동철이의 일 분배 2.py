import sys
sys.stdin = open('1865.txt', 'r')

T = int(input())
for tc in range(1, T+1):
	N = int(input())
	data = [list(map(int, input().split())) for _ in range(N)]
	for r in range(N):
		for c in range(N):
			data[r][c] = data[r][c]/100
	v = [0] * N
	arr = list(range(N))

	ans = 0
	def func(k, val):
		global ans
		if k == N:
			if val > ans:
				ans = val
		else:
			for i in range(N):
				if v[i]: continue
				v[i] = 1
				if val * data[k][arr[i]] > ans:
					func(k+1, val*data[k][arr[i]])
				v[i] = 0
	func(0, 1)
	print('#%d %0.6f' % (tc, ans * 100))

