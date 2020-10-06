# 재귀
def solution(n):
	answer = 0

	def func(i, val):
		nonlocal answer
		if val == n:
			answer += 1
			return
		else:
			if val + i + 1 <= n:
				func(i + 1, val + i + 1)

	for i in range(1, n + 1):
		func(i, i)

	return answer

# while문
def solution2(n):
	answer = 0

	for i in range(1, n+1):
		tmp = i
		while tmp < n:
			i += 1
			tmp += i

		if tmp == n:
			answer += 1

	return answer
