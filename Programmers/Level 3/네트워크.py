def solution(n, computers):
	answer = []
	for x in range(n):
		for y in range(n):
			if computers[x][y] == 1:
				answer.append([x, y])
				stack = [(x, y)]
				while stack:
					b, a = stack.pop()
					computers[b][a] = 0
					computers[a][b] = 0
					for c in range(n):
						if computers[a][c] == 1:
							stack += [(a, c)]
							answer[-1].append(c)
	return len(answer)

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))