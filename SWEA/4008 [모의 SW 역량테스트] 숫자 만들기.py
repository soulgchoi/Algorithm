import sys
sys.stdin = open('4008.txt', 'r')

#
# def func(k, val, op1, op2, op3, op4):
# 	global ans_min, ans_max, N
# 	if k == N:
# 		if val < ans_min:
# 			ans_min = val
# 		if val > ans_max:
# 			ans_max = val
# 	else:
# 		if op1 > 0:
# 			func(k + 1, val + numbers[k], op1 - 1, op2, op3, op4)
# 		if op2 > 0:
# 			func(k + 1, val - numbers[k], op1, op2 - 1, op3, op4)
# 		if op3 > 0:
# 			func(k + 1, val * numbers[k], op1, op2, op3 - 1, op4)
# 		if op4 > 0:
# 			func(k + 1, int(val / numbers[k]), op1, op2, op3, op4 - 1)
#
#
# T = int(input())
# for tc in range(1, T+1):
# 	N = int(input())
# 	op1, op2, op3, op4 = map(int, input().split())
# 	numbers = list(map(int, input().split()))
#
# 	ans_min = 10000000000
# 	ans_max = -10000000000
#
# 	func(1, numbers[0], op1, op2, op3, op4)
# 	print('#%d %d' % (tc, ans_max - ans_min))

T = int(input())
for tc in range(1, T+1):
	N = int(input())
	operators = list(map(int, input().split()))
	numbers = list(map(int, input().split()))

	ans_min = 10000000000
	ans_max = -10000000000

	def func(k, val):
		global ans_min, ans_max
		if k == N:
			if val < ans_min:
				ans_min = val
			if val > ans_max:
				ans_max = val
		else:
			for i in range(4):
				if operators[i] == 0: continue
				operators[i] -= 1
				t_val = func2(val, numbers[k], i)
				func(k+1, t_val)
				operators[i] += 1

	def func2(a, b, c):
		if c == 0:
			return a + b
		elif c == 1:
			return a - b
		elif c == 2:
			return a * b
		elif c == 3:
			return int(a/b)

	func(1, numbers[0])
	print('#%d %d' % (tc, ans_max - ans_min))