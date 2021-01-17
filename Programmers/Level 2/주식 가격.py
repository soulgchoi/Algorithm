def solution(prices):
	answer = [0] * len(prices)
	stack = [(prices[0], 0, 0)]
	sec = 1
	for p in range(1, len(prices)):
		while stack:
			if stack[-1][0] > prices[p]:
				answer[stack[-1][2]] = sec - stack[-1][1]
				stack.pop()
			else:
				break
		stack += [(prices[p], sec, p)]
		sec += 1

	while stack:
		temp = stack.pop()
		answer[temp[2]] = len(prices) - temp[2] - 1

	return answer


print(solution([1, 2, 3, 2, 3]))
print(solution([5, 8, 6, 2, 4, 1]))  # [3, 1, 1, 2, 1, 0]
