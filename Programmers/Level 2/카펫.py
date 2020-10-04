def solution(brown, yellow):
	carpet = brown + yellow
	divisor = []
	for c in range(3, carpet):
		if carpet // c < 3:
			continue
		if carpet % c == 0:
			if c > carpet // c:
				divisor += [(c, carpet // c)]
			else:
				divisor += [(carpet // c, c)]
	divisor = list(set(divisor))
	if len(divisor) == 1:
		return divisor[0]

	answer = []
	for d, v in divisor:
		tmp = v * 2 + (d - 2) * 2
		if d * v - tmp == yellow:
			answer += [d, v]
			break
	return answer
