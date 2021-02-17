def solution(people, limit):
	answer = 0
	people = sorted(people, reverse=True)
	left, right = 0, len(people)-1
	while left < right:
		if people[left] + people[right] <= limit:
			right -= 1
		left += 1
		answer += 1
	return answer if left != right else answer + 1


# print(solution([70, 50, 80, 50], 100))  # 3
# print(solution([70, 80, 50], 100))  # 3
