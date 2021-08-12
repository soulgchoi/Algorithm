import sys

sys.stdin = open('1260.txt', 'r')


def dfs(v):
    stack = [v]
    while stack:
        v = stack.pop()
        if not dfs_v[v - 1]:
            dfs_v[v - 1] = 1
            print(v, end=' ')
            for w in graph[v - 1]:
                if not dfs_v[w - 1]:
                    dfs(w)


def bfs(v):
    queue = [v]
    while queue:
        v = queue.pop(0)
        if not bfs_v[v - 1]:
            bfs_v[v - 1] = 1
            print(v, end=' ')
            for w in graph[v - 1]:
                queue += [w]


N, M, V = map(int, input().split(' '))

edges = [list(map(int, input().split(' '))) for _ in range(M)]
graph = [[] for _ in range(N)]

for edge in edges:
    graph[edge[0] - 1] += [edge[1]]
    graph[edge[1] - 1] += [edge[0]]

print(edges)

graph = [sorted(g) for g in graph]

dfs_v = [0] * N
bfs_v = [0] * N

dfs(V)
print()
bfs(V)
print()
