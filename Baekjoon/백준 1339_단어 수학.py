import sys
sys.stdin = open('1339.txt', 'r')

T = int(input())
for tc in range(1, T+1):
	print(f'--------------------{tc}-------------------------')

	N = int(input())
	words = [input() for _ in range(N)]
	w_max = max(len(x) for x in words)
	for w in range(N):
		words[w] = '0' * (w_max - len(words[w])) + words[w]

	M = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	alphabet = {}
	for m in M:
		alphabet[m] = '0'

	num = 9
	for i in range(w_max):
		for j in range(len(words)):
			word = words[j]
			if alphabet.get(word[i]) == '0':
				alphabet[word[i]] = str(num)
				num -= 1
			word = word[0:i] + alphabet.get(word[i], '0') + word[i+1:]
			words[j] = word

	answer = sum(list(map(int, words)))
	print(answer)
