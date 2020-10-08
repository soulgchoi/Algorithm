# 너무 어렵게 생각하면 안되는 문제였다~
def solution(n):
	answer = [[0]*m for m in range(1, n+1)]
	i, j, num = 0, 0, 1
	check = sum(c for c in range(1, n+1))
	while num < check:
		while i < n and answer[i][j] == 0:
			answer[i][j] = num
			i += 1
			num += 1
		i -= 1
		j += 1
		while 0 <= j < len(answer[i]) and answer[i][j] == 0:
			answer[i][j] = num
			j += 1
			num += 1
		j -= 2
		i -= 1
		while i >= 0 and j >= 0 and answer[i][j] == 0:
			answer[i][j] = num
			i -= 1
			j -= 1
			num += 1
		i += 2
		j += 1
	return sum(answer, [])


# def left(arr, num, idx_1, idx_2):
# 	while idx_1 < len(arr) and arr[idx_1][idx_2] == 0:
# 		arr[idx_1][idx_2] = num
# 		idx_1 += 1
# 		num += 1
# 	return arr, num - 1
#
#
# def right(arr, num, idx_1, idx_2):
# 	while idx_1 > 0 and arr[idx_1][idx_2] == 0:
# 		arr[idx_1][idx_2] = num
# 		idx_1 -= 1
# 		idx_2 -= 1
# 		num += 1
# 	return arr, num - 1
#
#
# def straight(arr, idx_1, idx_2, n, k):
# 	for i in range(idx_1, k):
# 		arr[idx_2][i] = n
# 		n += 1
# 	return arr, n - 1
#
#
# def solution(n):
# 	answer = answer = [[0]*m for m in range(1, n+1)]
# 	answer[0][0] = 1
# 	num = 1
# 	l_idx_1, l_idx_2 = 1, 0
# 	r_idx_1, r_idx_2 = n-2, len(answer[n-1])-2
# 	i = 0
# 	while sum(answer, []).count(0) > 0:
# 		answer, num = left(answer, num+1, l_idx_1, l_idx_2)
# 		l_idx_1, l_idx_2 = l_idx_1+1, l_idx_2+1
# 		answer, num = straight(answer, i, n-1-i, num, len(answer[n-1-i])-i)
# 		i += 1
# 		r_idx_2 = len(answer[n-1-i])-i
# 		answer, num = right(answer, num+1, r_idx_1, r_idx_2)
# 		r_idx_1 -= 1
# 	return answer
