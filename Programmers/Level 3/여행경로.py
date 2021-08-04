def solution(tickets):
	n = len(tickets)
	answer = []
	visited = [[0, 0] for _ in range(n)]
	print(visited)
	return answer


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
