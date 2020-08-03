def solution(numbers):
	str_arr = list(map(str, numbers))
	max_length = 0
	for num in str_arr:
		if len(num) > max_length:
			max_length = len(num)
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
