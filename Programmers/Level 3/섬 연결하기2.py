def solution(n, costs):
	parent = {}
	rank = {}

	def make_set(v):
		parent[v] = v
		rank[v] = 0

	def find(v):
		if parent[v] != v:
			parent[v] = find(parent[v])
		return parent[v]

	def union(v, u):
		root1 = find(v)
		root2 = find(u)

		if root1 != root2:
			if rank[root1] > rank[root2]:
				parent[root2] = root1
			else:
				parent[root1] = root2
				if rank[root1] == rank[root2]:
					rank[root2] += 1

	def kruskal(graph):
		for v in graph['vertices']:
			make_set(v)
		mst = 0

		edges = graph['edges']
		edges.sort(key=lambda x: x[2])

		for edge in edges:
			v, u, weight = edge

			if find(v) != find(u):
				union(v, u)
				mst += weight
		return mst
	graph = {
		'vertices': list(range(n)),
		'edges': costs
	}
	answer = kruskal(graph)
	return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))  # 4
print(solution(5, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]]))  # 15
print(solution(5, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 3], [2, 3, 8], [3, 4, 1]]))  # 7
