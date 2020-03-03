from itertools import permutations
import sys
sys.stdin = open('4008.txt', 'r')

T = int(input())
for tc in range(1, T+1):
	N = int(input())
	operators_input = list(map(int, input().split()))
	# + - * / 순서
	# 연산자 우선순위는 무시하고 앞부터 계산한다.
	numbers = list(map(int, input().split()))

	temp = ['*', '-', '*', '/']
	operators = []
	for idx, val in enumerate(temp):
		operators += [val] * operators_input[idx]
	print(operators)

	M = len(operators)
	v = [0]*M

	ans_min = 99999
	ans_max = 0
	def func(k, val):
		if k == N:
			if val < ans_min:
				ans_min = val
			elif val > ans_max:
				ans_max = val
		else:
			for i in range(M):
				if v[i]: continue
				t[k] = arr[i]
				v[i] = 1
				func(k+1, val)
				v[i] = 0

