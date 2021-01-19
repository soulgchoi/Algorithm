def solution2(bridge_length, weight, truck_weights):
	length = len(truck_weights)
	answer = 1
	front, rear = 0, 1
	bridge = [(truck_weights.pop(0), answer)]
	while front < length:
		answer += 1
		if answer - bridge[front][1] >= bridge_length:
			bridge[front] = (0, 0)
			front += 1
		if rear - front < bridge_length:
			if not truck_weights:
				continue
			bridge_weight = sum(list(map(lambda x: x[0], bridge)))
			if bridge_weight + truck_weights[0] <= weight:
				bridge += [(truck_weights.pop(0), answer)]
				rear += 1
	return answer


def solution(bridge_length, weight, truck_weights):
	answer = 0
	bridge = []
	bridge_count = []
	while True:
		answer += 1
		if bridge_count:
			bridge_count = list(map(lambda x: x+1, bridge_count))
			if bridge_count[0] >= bridge_length:
				bridge_count.pop(0)
				bridge.pop(0)
		if len(truck_weights) < 1:
			if sum(bridge_count) == 0:
				break
		if len(bridge) < bridge_length:
			if not truck_weights:
				continue
			if sum(bridge) + truck_weights[0] <= weight:
				bridge += [truck_weights.pop(0)]
				bridge_count += [0]
	return answer


# print(solution(2, 10, [7, 4, 5, 6]))  # 8
# print(solution(100, 100, [10]))  # 101
# print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))  # 110
