import sys
sys.stdin = open('1339.txt', 'r')

T = int(input())
for tc in range(1, T+1):
	print(f'--------------------{tc}-------------------------')

	N = int(input())
	words = [input() for _ in range(N)]

	M = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	alphabet = {}
	for m in M:
		alphabet[m] = 0

	for word in words:
		l = len(word)
		for w in range(l):
			alphabet[word[w]] += 10 ** (l - w - 1)

	alphabet = sorted(alphabet.items(), key=lambda x: x[1], reverse=True)

	answer = 0
	number = 9
	for a in alphabet:
		x, y = a
		if not y:
			break

		answer += number * y
		number -= 1
	print(answer)





# N = int(input())
# words = [input() for _ in range(N)]
# w_max = max(len(x) for x in words)
# for w in range(N):
# 	words[w] = '0' * (w_max - len(words[w])) + words[w]
#
# M = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# alphabet = {}
# for m in M:
# 	alphabet[m] = '0'
#
# num = 9
# for i in range(w_max):
# 	for j in range(len(words)):
# 		word = words[j]
# 		if alphabet.get(word[i], '*') == '0':
# 			alphabet[word[i]] = str(num)
# 			num -= 1
# 		word = word[0:i] + alphabet.get(word[i], '0') + word[i+1:]
# 		words[j] = word
#
# answer = sum(list(map(int, words)))
# print(answer)
