# 처음 푼 코드
def checkASCII(s):
	return 65 <= ord(s) <= 90


def solution(str1, str2):
	n = 65536
	str1, str2 = str1.upper(), str2.upper()
	dict1, dict2 = {}, {}

	for i in range(1, len(str1)):
		if checkASCII(str1[i - 1]) and checkASCII(str1[i]):
			if (str1[i - 1] + str1[i]) in dict1.keys():
				dict1[str1[i - 1] + str1[i]] += 1
			else:
				dict1[str1[i - 1] + str1[i]] = 1

	for j in range(1, len(str2)):
		if checkASCII(str2[j - 1]) and checkASCII(str2[j]):
			if (str2[j - 1] + str2[j]) in dict2.keys():
				dict2[str2[j - 1] + str2[j]] += 1
			else:
				dict2[str2[j - 1] + str2[j]] = 1

	if dict1 == dict2:
		return n
	else:
		union, inter = dict1, {}
		for key, val in dict2.items():
			if key in union.keys():
				if val > union[key]:
					inter[key] = union[key]
					union[key] = val
				else:
					inter[key] = val
			else:
				union[key] = val
		answer = sum(inter.values()) / sum(union.values()) * n
		return int(answer)


# 새로 알게 된 것들
# 파이썬에는 string.isalpha() 메서드가 있다.
# 집합 연산자 | 랑 & 를 어떻게 쓸까 했는데 원래 리스트에서 찾으면 됐던 것.
# collections 의 Counter 를 쓰기도 하는데, 이건 더 공부해서 추가해야겠다.
def solution(str1, str2):
	n = 65536
	arr1, arr2 = [], []
	# 아래 for 문도 한줄로 줄일 수 있긴 한데 그냥 넘겼다...
	for s1 in range(len(str1) - 1):
		if str1[s1:s1 + 2].isalpha():
			arr1 += [str1[s1:s1 + 2].upper()]
	for s2 in range(len(str2) - 1):
		if str2[s2:s2 + 2].isalpha():
			arr2 += [str2[s2:s2 + 2].upper()]

	union = set(arr1) | set(arr2)
	inter = set(arr1) & set(arr2)

	if union == inter == set():
		return n
	else:
		c_union = sum(max(arr1.count(u), arr2.count(u)) for u in union)
		c_inter = sum(min(arr1.count(i), arr2.count(i)) for i in inter)
		return int(c_inter / c_union * n)
