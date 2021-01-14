def solution(clothes):
	hash_map = {}
	for c in clothes:
		if c[1] in hash_map.keys():
			hash_map[c[1]] += [c[0]]
		else:
			hash_map[c[1]] = [c[0]]

	answer = 1
	for val in hash_map.values():
		answer *= len(val) + 1
	return answer - 1


# print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
# print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
# print(solution(	[["a", "a"], ["b", "b"], ["c", "c"]]))
