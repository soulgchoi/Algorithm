import sys
sys.stdin = open('1504.txt', 'r')


def Dijkstra(start, end):
    D = [INF] * (N + 1)
    D[start] = 0
    queue = [(start, 0)]
    while queue:
        n, d = queue.pop(0)
        if d > D[n]:
            continue
        for v, w in graph[n]:
            if D[n] + w < D[v]:
                D[v] = D[n] + w
                queue += [(v, D[v])]

    return D[end]


# def Dijkstra(r, e):
#     D = [INF] * (N + 1)
#     D[r] = 0
#     for _ in range(N + 1):
#         min_idx = 0
#         m = INF
#         for i in range(N + 1):
#             if D[i] < m:
#                 m = D[i]
#                 min_idx = i
#             for v, val in graph[min_idx]:
#                 if D[min_idx] + val < D[v]:
#                     D[v] = D[min_idx] + val
#     return D[e]


N, E = map(int, input().split(' '))
nodes = [list(map(int, input().split(' '))) for _ in range(E)]
v1, v2 = map(int, input().split(' '))
INF = 0xffffff

graph = [[] for _ in range(N + 1)]
for node in nodes:
    a, b, c = node
    graph[a] += [(b, c)]
    graph[b] += [(a, c)]

r1 = Dijkstra(1, v1) + Dijkstra(v1, v2) + Dijkstra(v2, N)
r2 = Dijkstra(1, v2) + Dijkstra(v2, v1) + Dijkstra(v1, N)

if r1 >= INF and r2 >= INF:
    print(-1)
else:
    print(min(r1, r2))
