import sys
sys.stdin = open('2819.txt', 'r')

T = int(input())
for tc in range(1, T+1):
	arr = [list(input().split()) for _ in range(4)]
	ans = set()
	dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

	def func(x, y, k, numbers=''):
		global ans
		if k == 7:
			ans.add(numbers)
		else:
			for dx, dy in dxdy:
				nx, ny = x + dx, y + dy
				if 0 <= nx < 4 and 0 <= ny < 4:
					func(nx, ny, k+1, numbers+arr[nx][ny])

	for r in range(4):
		for c in range(4):
			func(r, c, 0)

	print('#%d %d' % (tc, len(ans)))

