def solution2(progresses, speeds):
	answer = []
	front = 0
	while front < len(progresses):
		for i in range(front, len(progresses)):
			progresses[i] += speeds[i]

		done = 0
		while front < len(progresses):
			if progresses[front] >= 100:
				front += 1
				done += 1
			else:
				break
		if done > 0:
			answer += [done]

	return answer


def solution(progresses, speeds):
	answer = []
	front = 0
	day = 1
	done = 0
	while front < len(progresses):
		if progresses[front] + speeds[front] * day >= 100:
			done += 1
			front += 1
			continue
		else:
			answer += [done]
			day += 1
			done = 0
	answer += [done]
	return list(filter(lambda x: x > 0, answer))


# print(solution([93, 30, 55], [1, 30, 5]))
# print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
# print(solution([95, 95, 95, 95], [4, 3, 2, 1]))
