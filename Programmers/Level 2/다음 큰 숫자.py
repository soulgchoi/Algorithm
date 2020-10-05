def solution(n):
	answer = 0
	bin_n = str(bin(n)[2:])
	while True:
		n += 1
		if str(bin(n)[2:]).count('1') == bin_n.count('1'):
			answer = n
			break
	return answer
