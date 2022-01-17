def solution(N, road, K):
    graph = [[] for _ in range(N)]
    for i in range(len(road)):
        v1, v2, w = road[i]
        graph[v1-1] += [(v2-1, w)]
        graph[v2-1] += [(v1-1, w)]

    dis = [2 ** 31] * N
    path = [0] * N

    queue = [(0, 0)]
    dis[0] = 0
    while queue:
        v, w = queue.pop(0)
        if dis[v] < w:
            continue
        for edge in graph[v]:
            next_v, next_w = edge[0], edge[1]
            if w + next_w < dis[next_v]:
                dis[next_v] = w + next_w
                queue += [(next_v, dis[next_v])]
                path[next_v] = v

    return len(list(filter(lambda x: x <= K, dis)))


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))