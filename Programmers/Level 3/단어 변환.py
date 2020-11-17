def func(pre_word, words, d, v):
	global t, answer
	if pre_word == t:
		if d < answer:
			answer = d

	for w in range(len(words)):
		dif = 0
		for i in range(len(pre_word)):
			if pre_word[i] != words[w][i]:
				dif += 1

		if dif == 1 and not v[w]:
			v[w] = 1
			func(words[w], words, d + 1, v)
			v[w] = 0


def solution(begin, target, words):
	global t, answer
	answer = 50
	t = target
	v = [0] * len(words)
	func(begin, words, 0, v)
	return answer if answer < 50 else 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
print(solution("hit", "hhh", ["hhh", "hht"]))