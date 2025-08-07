import sys
from math import inf

sys.setrecursionlimit(22222)


def dfs_dist(i, p):
    for j, w in G[i]:
        if j != p:
            dist[j] = dist[i] + w
            dfs_dist(j, i)


def dfs_parent(i, p):
    for j, _ in G[i]:
        if j != p:
            parent[j] = i
            dfs_parent(j, i)


N = int(input())
G = [[] for _ in range(N + 1)]

for i in range(2, N + 1):
    a, w = map(int, input().split())
    G[i].append((a, w))
    G[a].append((i, w))

dist = [0] * (N + 1)
dfs_dist(1, 0)
u = max(range(1, N + 1), key=lambda x: dist[x])

dist = [0] * (N + 1)
dfs_dist(u, 0)
v = max(range(1, N + 1), key=lambda x: dist[x])

parent = [0] * (N + 1)
dfs_parent(u, 0)

res = inf
i = v

while i:
    res = min(res, max(dist[i], dist[v] - dist[i]))
    i = parent[i]

print(res)
