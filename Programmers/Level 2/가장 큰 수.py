# 틀림
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


# 몇 개 테스트케이스가 시간초과
def compare(a, b):
	if int(b + a) - int(a + b) > 0:
		return True
	else:
		return False

def solution2(numbers):
	str_arr = list(map(str, numbers))
	str_arr.sort(key=lambda x:x[0], reverse=True)
	flag = 0
	while flag != len(numbers) - 1:
		flag = 0
		for i in range(len(numbers) - 1):
			if not compare(str_arr[i], str_arr[i+1]):
				flag += 1
			else:
				str_arr[i], str_arr[i+1] = str_arr[i+1], str_arr[i]
	return '0' if str_arr[0] == '0' else ''.join(str_arr)


# 람다와 cmp_to_key 를 좀 더 봐야겠다 싶은 코드..
# cpm_to_key 는 고차 함수를 반환한다.
def solution3(numbers):
	import functools
	answer = list(map(str, numbers))
	answer.sort(key=functools.cmp_to_key(lambda a, b: int(b+a)-int(a+b)))
	return '0' if answer[0] == '0' else ''.join(answer)
