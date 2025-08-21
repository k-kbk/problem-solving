import sys
from math import ceil, inf
from heapq import heappop, heappush

input = sys.stdin.readline

N, M = map(int, input().split())
S, E, C = map(int, input().split())
S -= 1
E -= 1
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b, k = map(int, input().split())
    a -= 1
    b -= 1
    cost = ceil(C / k)
    graph[a].append((b, cost))
    graph[b].append((a, cost))

pq = []
heappush(pq, (0, S))
dist = [inf] * N
dist[S] = 0

while pq:
    d, u = heappop(pq)
    if dist[u] < d:
        continue
    for v, w in graph[u]:
        if dist[v] > d + w:
            dist[v] = d + w
            heappush(pq, (dist[v], v))

if dist[E] < inf:
    print(dist[E])
else:
    print(-1)
