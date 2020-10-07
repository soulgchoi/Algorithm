# 간단버전
def solution(s):
	s = s[2:-2].split('},{')
	s.sort(key=len)

	ans = []
	for t in range(len(s)):
		s[t] = s[t].split(',')
		for u in s[t]:
			if u not in ans:  # int 처리를 여기서 해도 크게 차이는 없는 것 같다
				ans += [u]
	return list(map(int, ans))


# 뭐 이렇게 풀어야 하는지.. 좀 간단하게 해야겠다
def solution(s):
	s = s[1:-1].replace('{', '').split('}')
	for t in range(len(s)):
		s[t] = s[t].split(',')
		if s[t][0] == '':
			s[t] = s[t][1:]
	s.pop()
	s = sorted([list(map(int, u)) for u in s], key=len)

	ans = []
	for i in s:
		for j in i:
			if j not in ans:
				ans.append(j)
	return ans