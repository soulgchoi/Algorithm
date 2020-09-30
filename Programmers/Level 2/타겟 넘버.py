def solution(numbers, target):
	answer = []

	def bfs(val, depth):
		if depth == len(numbers):
			if val == target:
				answer.append(1) # answer += 1 은 할당이라 안된다.. global도 안된다..
				return
		else:
			bfs(val + numbers[depth], depth + 1)
			bfs(val - numbers[depth], depth + 1)

	bfs(0, 0)
	return len(answer)