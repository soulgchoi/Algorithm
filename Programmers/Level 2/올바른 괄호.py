def solution(s):
	cnt = 0
	if s[0] == ')':
		return False
	else:
		cnt = 1

	i = 1
	while i < len(s):
		if s[i] == '(':
			cnt += 1
		if s[i] == ')':
			if cnt == 0:
				return False
			else:
				cnt -= 1
		i += 1
	return False if cnt > 0 else True
