def solution(n, edge):
    graph = [[] for _ in range(n)]
    for s, t in edge:
        graph[s - 1] += [t - 1]
        graph[t - 1] += [s - 1]

    path = [n * n] * n
    path[0] = 0
    stack = [0]
    while stack:
        v = stack.pop(0)
        for e in graph[v]:
            dis = path[v] + 1
            if dis < path[e]:
                path[e] = dis
                stack += [e]

    return path.count(max(path))


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
