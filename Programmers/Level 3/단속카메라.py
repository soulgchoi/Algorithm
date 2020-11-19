def solution(routes):
	answer = 1
	routes.sort(key=lambda x: x[1])
	camera = routes[0][1]

	r = 1
	while r < len(routes):
		if routes[r][0] > camera:
			camera = routes[r][1]
			answer += 1
		r += 1

	return answer


# print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))
# print(solution([[-2,-1], [1,2],[-3,0]])) #2
# print(solution([[0,0],])) #1
# print(solution([[0,1], [0,1], [1,2]])) #1
# print(solution([[0,1], [2,3], [4,5], [6,7]])) #4
# print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])) #2
# print(solution([[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2
# print(solution([[0,12],[1,12],[2,12],[3,12],[5,6],[6,12],[10,12]]))