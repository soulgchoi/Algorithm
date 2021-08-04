def solution(n, costs):
	answer = 10 ** 4 * 9
	island = [[0] * n for _ in range(n)]
	for cost in costs:
		island[cost[0]][cost[1]] = cost[2]
		island[cost[1]][cost[0]] = cost[2]

	for r in range(n):
		for c in range(n):
			if island[r][c] > 0:

				def func(y, val, li):
					nonlocal answer
					if len(li) == n:
						if val < answer:
							answer = val
							return

					for z in range(n):
						if z not in li and island[y][z] > 0:
							li += [z]
							if val + island[y][z] < answer:
								func(z, val + island[y][z], li)
							li.remove(z)

				func(c, island[r][c], [r, c])

	return answer


"""
def solution(n, costs):
	answer = 10 ** 4 * 9
	island = [[0] * n for _ in range(n)]
	for cost in costs:
		island[cost[0]][cost[1]] = cost[2]
		island[cost[1]][cost[0]] = cost[2]

	for r in range(n):
		for c in range(n):
			if island[r][c] > 0:
				tmp_cost = island[r][c]
				li = [r, c]
				stack = [(r, c)]

				while stack:
					x, y = stack.pop()
					for z in range(n):
						if island[y][z] > 0 and z not in li:
							tmp_cost += island[y][z]
							li += [z]
							stack += [(y, z)]

						if len(li) == n:
							if tmp_cost < answer:
								answer = tmp_cost
							break
	return answer
"""

# print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
print(solution(5, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 3], [2, 3, 8], [3, 4, 1]]))
print(solution(4, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4]]))
print(solution(4, [[0, 1, 1], [0, 2, 2], [2, 3, 1]]))
