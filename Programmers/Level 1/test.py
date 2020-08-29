def solution(n):
	answer = 0
	if n >= 2:
		answer += 1
	numbers = list(range(3, n + 1, 2))
	for number in numbers:
		flag = True
		for num in range(3, number, 2):
			if not number % num:
				flag = False
				break
		if flag:
			answer += 1
	return answer

n = 5
print(solution(n))