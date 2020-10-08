# 비교를 해야하나 했는데.. 딱 그대로 곱하면 되는 케이스만 나오는듯
def solution(arr1, arr2):
	answer = arr3 = [[0] * len(arr2[0]) for _ in range(len(arr1))]
	for i in range(len(arr1)):
		for j in range(len(arr2[0])):
			for n in range(len(arr1[0])):
				arr3[i][j] += arr1[i][n] * arr2[n][j]
	return answer
