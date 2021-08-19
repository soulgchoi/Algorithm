import sys

sys.stdin = open('1238.txt', 'r')


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


N, M, X = map(int, input().split(' '))
nodes = [list(map(int, input().split(' '))) for _ in range(M)]

graph = [[] for _ in range(N + 1)]
for node in nodes:
    a, b, c = node
    graph[a] += [(b, c)]

INF = 0xffffff

answer = 0
for n in range(1, N + 1):
    if n == X:
        continue
    d1 = Dijkstra(n, X)
    d2 = Dijkstra(X, n)
    if d1 + d2 > answer:
        answer = d1 + d2

print(answer)
