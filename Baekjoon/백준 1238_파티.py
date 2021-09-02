import sys

sys.stdin = open('1238.txt', 'r')


def Dijkstra(G, start):
    D = [INF] * (N + 1)
    D[start] = 0
    queue = [(start, 0)]
    while queue:
        n, d = queue.pop(0)
        if d > D[n]:
            continue
        for v, w in G[n]:
            if D[n] + w < D[v]:
                D[v] = D[n] + w
                queue += [(v, D[v])]

    return D


N, M, X = map(int, input().split(' '))
nodes = [list(map(int, input().split(' '))) for _ in range(M)]

graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]
for node in nodes:
    a, b, c = node
    graph[a] += [(b, c)]
    reverse_graph[b] += [(a, c)]

INF = 0xffffff

answer = 0
# for n in range(1, N + 1):
#     if n == X:
#         continue
d1 = Dijkstra(graph, X)
d2 = Dijkstra(reverse_graph, X)
for i in range(1, N+1):
    if d1[i] + d2[i] > answer:
        answer = d1[i] + d2[i]

print(answer)
