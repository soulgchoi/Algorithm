# def quickSort(array):
# 	if len(array) < 2:
# 		return array
#
# 	pivot = str(array[len(array)-1])
# 	left, right = [], []
#
# 	for i in range(0, len(array)-1):
# 		stringifiedNum = str(array[i])
# 		if stringifiedNum[0] > pivot[0]:
# 			left.append(stringifiedNum)
# 		elif stringifiedNum[0] == pivot[0]:
# 			if len(stringifiedNum) > len(pivot):
# 				for j in range(0, len(pivot)):
# 					if stringifiedNum[j+1] > pivot[j]:
# 						left.append(stringifiedNum)
# 					else:
# 						right.append(stringifiedNum)
# 			elif len(stringifiedNum) < len(pivot):
# 				for j in range(0, len(stringifiedNum)):
# 					if stringifiedNum[j] > pivot[j+1]:
# 						left.append(stringifiedNum)
# 					else:
# 						right.append(stringifiedNum)
# 			elif len(stringifiedNum) == len(pivot):
# 				for j in range(1, len(stringifiedNum)):
# 					if stringifiedNum[j] > pivot[j]:
# 						left.append(stringifiedNum)
# 					else:
# 						right.append(stringifiedNum)
# 		else:
# 			right.append(stringifiedNum)
#
# 	return [quickSort(left), pivot, quickSort(right)]
#
# def solution(numbers):
# 	answer = quickSort(numbers)
# 	print(answer)
# 	return answer
#
# solution([3, 30, 34, 5, 9])

# def solution(numbers):
# 	str_arr = list(map(str, numbers))
# 	max_length = 0
# 	for num in str_arr:
# 		if len(num) > max_length:
# 			max_length = len(num)
# 	sorted_arr = []
# 	for idx, num in enumerate(str_arr):
# 		if len(num) < max_length:
# 			num += num[0] * (max_length - len(num))
# 		sorted_arr += [[int(num), idx]]
# 	sorted_arr.sort(key=lambda x: -x[0])
# 	answer = []
# 	for num in sorted_arr:
# 		answer += str_arr[num[1]]
# 	return '0' if answer[0] == '0' else ''.join(answer)

def solution(numbers):
	str_arr = list(map(str, numbers))
	max_length = 4
	sorted_arr = []
	for idx, num in enumerate(str_arr):
		if len(num) < max_length:
			num += num[0] * (max_length - len(num))
		sorted_arr += [[int(num), idx]]
	sorted_arr.sort(key=lambda x: -x[0])
	answer = []
	for num in sorted_arr:
		answer += str_arr[num[1]]
	return '0' if answer[0] == '0' else ''.join(answer)
