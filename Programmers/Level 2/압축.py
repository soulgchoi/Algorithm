def solution(msg):
	answer = []
	dictionary = [chr(i) for i in range(ord('A'), ord('Z')+1)]
	while len(msg) > 0:
		for i in range(len(msg), -1, -1):
			if msg[:i] in dictionary:
				answer.append(dictionary.index(msg[:i]))
				dictionary.append(msg[:i+1])
				msg = msg[i:]
				break
	return list(map(lambda x: x+1, answer))


print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))