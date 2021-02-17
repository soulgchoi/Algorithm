def solution(number, k):
	number = [n for n in number]
	answer = ""
	for i in range(len(number)):
		if not answer:
			answer += number[i]
			continue
		while k > 0 and answer and answer[-1] < number[i]:
			answer = answer[:-1]
			k -= 1
		answer += number[i]
	return answer[:-k] if k else answer



# print(solution("1924", 2))  # "94"
# print(solution("1321234", 3))  # "3234"
print(solution("4177252841", 4))  # "775841"
print(solution("01010", 3))
