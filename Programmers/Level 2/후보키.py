def powerset(s):
	r = [[]]

	for e in s:
		temp = [x + [e] for x in r]
		r += temp
	return r


def isUnique(arr, idx):
	tmp = []

	for i in range(len(arr)):
		check = []
		for j in idx:
			check += [arr[i][j]]

		if check in tmp:
			return False
		else:
			tmp += [check]
	else:
		return True


def solution(relation):
	answer = 0
	c = 0
	combs = powerset(list(range(len(relation[0]))))[1:]
	combs.sort(key=len)
	while c < len(combs):
		if isUnique(relation, combs[c]):
			x = c + 1
			# 최소성을 판별하는 부분
			while x < len(combs):
				y = len(combs[c])
				z = 0
				for a in combs[c]:
					if a in combs[x]:
						z += 1
				if z == y:  # 현재 조합 요소를 모두 가지고 있는 조합을 제거한다.
					combs.remove(combs[x])
				else:
					x += 1
			answer += 1
		c += 1
	return answer

# solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]])
# solution([['a', 'b', 'c'], ['1', 'b', 'c'], ['a', 'b', '4'], ['a', '5', 'c']])