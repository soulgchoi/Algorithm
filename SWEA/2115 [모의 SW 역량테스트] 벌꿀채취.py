import sys
sys.stdin= open('2115 [모의 SW 역량테스트] 벌꿀채취.txt', 'r')

# def powerset():
# 	numbers = [1, 2, 3, 4]
# 	r = [[]]
#
# 	for e in numbers:
# 		temp = [x + [e] for x in r]
# 		r += temp
# 	return r
#
# print(powerset())

T = int(input())
for tc in range(1, T+1):
	N, M, C = map(int, input().split())
	honey = [list(map(int, input().split())) for _ in range(N)]
	# print(*honey, sep='\n')
	
	# N * N 의 벌꿀
	# 두 명이 채취한다.
	# 두 명이 각각,
	# 가로로 연속한 M 칸에서 채취해야 한다.
	# 겹치면 안된다.
	# 최종 수익은 각 칸의 꿀 제곱의 합이다.
	# 최대 C 만큼 채취할 수 있다.
	# M 칸에서 모두 채취할 때 C 를 넘으면,
	# C 를 넘지 않는 선에서 칸을 선택한다. ( 부분집합 )

	honeyPot = [[0]*N for _ in range(N)]
	# print(honeyPot)

	# max1 = (0, 0, 0)
	for row in range(N):
		for col in range(N-M+1):
			bee = honey[row][col:col+M]
			if sum(bee) > C:
				temp_sum = 0
				powerset = [[]]
				for b in bee:
					temp = [x + [b] for x in powerset]
					powerset += temp
				for p in powerset:
					if sum(p) <= C:
						sum_p = 0
						for pp in p:
							sum_p += pp ** 2
						if temp_sum < sum_p:
							temp_sum = sum_p
							bee = p
			for e in bee:
				honeyPot[row][col] += e**2
		sum_honey = (0, 0)
		for col2 in range(N-M+1):
			if honeyPot[row][col2] > sum_honey[0]:
				sum_honey = honeyPot[row][col2], col2
		for i in range(sum_honey[1]-M+1, sum_honey[1]+M):
			honeyPot[row][i] = 0
		honeyPot[row][sum_honey[1]] = sum_honey[0]
		# if sum_honey[0] > max1[0]:
		# 	max1 = sum_honey[0], row, sum_honey[1]

	# honeyPot[max1[1]][max1[2]] = 0
	# max2 = max(sum(honeyPot, []))
	honeyPot2 = sorted(sum(honeyPot, []), reverse=True)
	print('#%d %d' % (tc, honeyPot2[0] + honeyPot2[1]))


