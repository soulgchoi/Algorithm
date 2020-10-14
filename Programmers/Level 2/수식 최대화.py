def cal(op, num1, num2):
	if op == '+':
		return num1 + num2
	elif op == '-':
		return num1 - num2
	elif op == '*':
		return num1 * num2


def solution(expression):
	answer = 0
	priors = [('*', '+', '-'), ('+', '-', '*'), ('+', '*', '-'), ('-', '+', '*'), ('-', '*', '-'), ('*', '-', '+')]
	numbers, operands = [], []
	tmp = ''
	for e in expression:
		if e in '+-*':
			numbers += [int(tmp)]
			numbers += [e]
			tmp = ''
		else:
			tmp += e
	numbers += [int(tmp)]

	for p in priors:
		_numbers = numbers[:]
		for operand in range(3):
			i = 1
			while len(_numbers) > 1 and p[operand] in _numbers:
				if _numbers[i] == p[operand]:
					_numbers[i-1] = cal(_numbers[i], _numbers[i-1], _numbers[i+1])
					_numbers.pop(i)
					_numbers.pop(i)
				else:
					if i == len(_numbers):
						i = 1
					else:
						i += 1
		if abs(_numbers[0]) > answer:
			answer = abs(_numbers[0])

	return answer
