import sys
sys.stdin = open('2112 [모의 SW 역량테스트] 보호 필름.txt', 'r')

T = int(input())
for tc in range(1, T+1):
	D, W, K = map(int, input().split())
	data = [list(map(int, input().split())) for _ in range(D)]

	# 아래로만 가는 dfs
	# 약품 투입 횟수
	# 언제 넣지?
	# 최초는 검증, 하나 안되면 멈추고
	# 약품 넣어보기
	# 약품을 A 로 넣을지 B 로 넣을지
	# 약품 0 > 1 > 2 중에 되면 stop, 최소 횟수를 구하므로
	# 약품 넣는 경우의 수는 1 + D*2 + sum(range(1, D))

	def dfs(x, y, cnt, val, ls):  # val == data[x][y]
		while x + 1 < D:
			nx = x + 1
			if ls[nx][y] == val:
				x = nx
				cnt += 1
			else:
				x, val = nx, ls[nx][y]
				cnt = 1

			if cnt == K:
				return 1
		return 0

	# 품질검증
	def func(ls):
		k = 0
		for w in range(W):
			if dfs(0, w, 1, ls[0][w], ls):
				k += 1
			else:
				return 0
		return 1

	def func3(i, ans, ls):
		global res, A, B
		if func(ls):
			if ans < res:
				res = ans
			return
		else:
			for j in range(i, D):
				temp = ls[j]
				ls[j] = A
				func3(j+1, ans+1, ls)
				ls[j] = B
				func3(j+1, ans+1, ls)
				ls[j] = temp

	res = 99999
	A = [0] * W
	B = [1] * W
	func3(0, 0, data)
	print('#%d %d' % (tc, res))