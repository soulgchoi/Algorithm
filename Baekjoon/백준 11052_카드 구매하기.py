import sys
sys.stdin = open('11052.txt', 'r')

T = int(input())
for tc in range(1, T+1):
	print(f'--------------------{tc}-------------------------')

	N = int(input())
	P = list(map(int, input().split()))
	P = [0] + P
	print(f'카드팩: {P}')

	costs = [0] * (N + 1)

	for i in range(1, N+1):
		costs[i] = P[i]
		for j in range(1, i//2 + 1):
			costs[i] = max(costs[i], costs[j] + costs[i-j])
	print(costs)
	print(costs[-1])

