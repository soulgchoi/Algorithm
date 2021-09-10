import heapq


def dijkstra(N, graph, start, end):
    dist = [200 * 100000] * N
    pq = [(start, 0)]
    heapq.heapify(pq)
    dist[start] = 0
    while pq:
        n, d = heapq.heappop(pq)
        if dist[n] < d:
            continue
        for v, w in graph[n]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq, (v, dist[v]))
    return dist[end]


def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n)]
    s, a, b, = s-1, a-1, b-1
    for fare in fares:
        v1, v2, w = fare
        graph[v1-1] += [(v2-1, w)]
        graph[v2-1] += [(v1-1, w)]

    cost = dijkstra(n, graph, s, a) + dijkstra(n, graph, s, b)
    for m in range(n):
        if s == m:
            continue
        cost2 = dijkstra(n, graph, s, m) + + dijkstra(n, graph, m, a) + dijkstra(n, graph, m, b)
        if cost2 < cost:
            cost = cost2
    return cost


print(solution(6, 4, 6, 2,
    [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))  # 82
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))  # 14
print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))  # 18
