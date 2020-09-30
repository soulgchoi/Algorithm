def solution(numbers, target):
	answer = []

	def bfs(val, depth):
		if depth == len(numbers):
			if val == target:
				answer.append(1) # answer += 1 은 할당이라 안된다.. global도 안된다..
				return
		else:
			bfs(val + numbers[depth], depth + 1)
			bfs(val - numbers[depth], depth + 1)

	bfs(0, 0)
	return len(answer)

#
answer = 0

def bfs(arr, val, depth, k, tg, cnt):
    global answer
    if depth == k:
        if val == tg:
            answer += 1
            return cnt
    else:
        bfs(arr, val + arr[depth], depth + 1, k, tg, cnt)
        bfs(arr, val - arr[depth], depth + 1, k, tg, cnt)

def solution(numbers, target):
    global answer
    bfs(numbers, 0, 0, len(numbers), target, 0)
    return answer