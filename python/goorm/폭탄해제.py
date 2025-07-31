import sys

input = sys.stdin.readline

N, M = map(int, input().split())
edges = []
degree = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    edges.append((u, v))
    degree[u] += 1
    degree[v] += 1

res = [i + 1 for i, (u, v) in enumerate(edges) if degree[u] > 1 and degree[v] > 1]
print(*res if res else [-1])
