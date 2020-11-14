def solution(n, t, m, p):
	answer = '0'
	number = t * m
	for num in range(number):
		tmp = ''
		while num > 0:
			num, mod = divmod(num, n)
			if mod in range(10, 16):
				tmp += chr(mod + 55)
			else:
				tmp += str(mod)
		answer += tmp[::-1]
	return ''.join(list(answer[x] for x in range(p-1, len(answer), m)))[:t]



print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))
