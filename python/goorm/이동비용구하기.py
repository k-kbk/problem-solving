import sys, heapq

input = sys.stdin.readline

N, M = map(int, input().split())
S = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

dist = [float("inf")] * (N + 1)
dist[S] = 0
pq = [(0, S)]

while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for v, w in graph[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

answer = 0

for i in range(1, N + 1):
    if dist[i] == float("inf"):
        answer += -1
    else:
        answer += dist[i]

print(answer)
