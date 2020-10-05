# 테스트 케이스는 맞는데 실행하면 런타임 에러
# 재귀가 아니라 dp로 풀어야 하는 것 같다..
def solution(land):
	ans = []

	def func(arr, k, val, pre_idx):
		if k == len(arr):
			ans.append(val)
			return
		else:
			for i in range(4):
				if i != pre_idx:
					func(arr, k + 1, val + arr[k][i], i)

	func(land, 0, 0, 5)
	return max(ans)