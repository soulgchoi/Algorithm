import math
import heapq


def solution(jobs):
	answer = []
	queue = []
	hard_disk = []
	sec = 0

	jobs.sort(key=lambda x: (x[0], x[1]))

	while jobs + queue + hard_disk:
		while jobs:
			if jobs[0][0] <= sec:
				temp = jobs.pop(0)
				heapq.heappush(queue, temp)
			else:
				break

		if hard_disk:
			if sec == (hard_disk[1] + hard_disk[2]):
				answer += [sec - hard_disk[0]]
				hard_disk = []

		if not hard_disk and queue:
			temp = 0
			if len(queue) > 1:
				queue.sort(key=lambda x: x[1])
				temp = heapq.heappop(queue)
			else:
				temp = heapq.heappop(queue)
			hard_disk += temp + [sec]

		sec += 1

	return math.floor(sum(answer) / len(answer))


# print(solution([[0, 3], [1, 9], [2, 6]]))  # 9
# print(solution([[0, 3], [2, 6], [2, 2], [1, 9]]))
# print(solution([[0, 4], [1, 2], [5, 2]]))  # 4
# print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]))  # 14
# print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]))  # 25
# print(solution([[0, 3], [1, 9], [2, 6]]))  # 9
# print(solution([[0, 1]]))  # 1
# print(solution([[1000, 1000]]))  # 1000
# print(solution([[0, 1], [0, 1], [0, 1]]))  # 2
# print(solution([[0, 1], [0, 1], [0, 1], [0, 1]]))  # 2
# print(solution([[0, 1], [1000, 1000]]))  # 500
# print(solution([[100, 100], [1000, 1000]]))  # 550
# print(solution([[10, 10], [30, 10], [50, 2], [51, 2]]))  # 6
# print(solution([[0, 3], [1, 9], [2, 6], [30, 3]]))  # 7
# print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))  # 72

# def solution(jobs):
# 	answer = []
# 	queue = []
# 	hard_disk = []
# 	sec = 0
#
# 	jobs.sort(key=lambda x: (x[0], x[1]))
#
# 	while jobs + queue + hard_disk:
# 		while jobs:
# 			if jobs[0][0] <= sec:
# 				queue += [jobs.pop(0)]
# 			else:
# 				break
#
# 		if hard_disk:
# 			if sec == (hard_disk[1] + hard_disk[2]):
# 				answer += [sec - hard_disk[0]]
# 				hard_disk = []
#
# 		if not hard_disk and queue:
# 			temp = 0
# 			if len(queue) > 1:
# 				a = queue[0]
# 				b = queue[1]
# 				a_time = sec-a[0] + a[1]
# 				b_time = sec-b[0] + b[1]
# 				a_b = math.trunc((a_time + b_time + a[1] + sum(answer)) / (len(answer) + 2))
# 				b_a = math.trunc((a_time + b_time + b[1] + sum(answer)) / (len(answer) + 2))
# 				if a_b < b_a:
# 					temp = queue.pop(0)
# 				else:
# 					temp = queue.pop(1)
# 			else:
# 				temp = queue.pop(0)
# 			hard_disk += temp + [sec]
#
# 		sec += 1
#
# 	return math.trunc(sum(answer) / len(answer))
