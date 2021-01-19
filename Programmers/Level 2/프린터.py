def solution2(priorities, location):
	answer = 0
	while priorities:
		J = priorities.pop(0)
		if list(filter(lambda x: x > J, priorities)):
			priorities += [J]
			if location == 0:
				location = len(priorities) - 1
			else:
				location -= 1
		else:
			answer += 1
			if location == 0:
				return answer
			location -= 1
			continue
	return answer


def solution(priorities, location):
	answer = 0
	while priorities:
		J = priorities.pop(0)
		if (priorities and max(J, max(priorities)) == J) or (not priorities):
			answer += 1
			if location == 0:
				return answer
			location -= 1
			continue
		else:
			priorities += [J]
			if location == 0:
				location = len(priorities) - 1
			else:
				location -= 1
	return answer


def solution3(priorities, location):
	answer = 0
	while priorities:
		J = priorities.pop(0)
		flag = False
		for p in priorities:
			if p > J:
				flag = True
				break
		if flag:
			priorities += [J]
			if location == 0:
				location = len(priorities) - 1
			else:
				location -= 1
		else:
			answer += 1
			if location == 0:
				return answer
			location -= 1
			continue
	return answer


# print(solution([2, 1, 3, 2], 2))  # 1
# print(solution([1, 1, 9, 1, 1, 1], 0))  # 5
