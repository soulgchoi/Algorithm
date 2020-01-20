import sys
sys.stdin = open('16235.txt', 'r')

T = int(input())
for tc in range(1, T+1):
	N, M, K = map(int, input().split())  # N 줄의 배열, 나무 위치 M 줄, K 년 후
	bob = [list(map(int, input().split())) for _ in range(N)]  # 배열
	tree_info = [list(map(int, input().split())) for _ in range(M)]
	for m in range(M):
		a3, b3, c3 = tree_info[m]
		tree_info[m] = [a3-1, b3-1, c3]
	ddang = [[5] * N for _ in range(N)]
	dxdy = [(1, 0), (-1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, -1)]

	tree_arr = [[[] for _ in range(N)] for _ in range(N)]
	for a, b, c in tree_info:
		tree_arr[a][b] += [c]

	print(tree_arr)
	k = 0
	while k < K:
		for t in range(N):
			for r in range(N):
				if len(tree_arr[t][r]) > 0:
					temp = []
					for tree in range(len(tree_arr[t][r])):
						if ddang[t][r] >= tree_arr[t][r][tree]:
							ddang[t][r] -= tree_arr[t][r][tree]
							tree_arr[t][r][tree] += 1
						else:
							temp += [tree_arr[t][r].pop(tree) // 2]
					ddang[t][r] += sum(temp)
		for t2 in range(N):
			for r2 in range(N):
				if len(tree_arr[t][r]) > 0:
					for tree2 in tree_arr[t][r]:
						if tree2 % 5 == 0:
							for dt, dr in dxdy:
								nt, nr = t + dt, r + dr
								if 0 <= nt < N and 0 <= nr < N:
									tree_arr[nt][nr].insert(0, [1])
				ddang[t2][r2] += bob[t2][r2]
		k += 1

	print(tree_arr)


			

