from collections import defaultdict

N, M, K = map(int, input().split())
graph = defaultdict(list)
visited = [False] * (N + 1)

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for v in graph:
    graph[v].sort()

visited[K] = True
count = 1

while True:
    for nxt in graph[K]:
        if not visited[nxt]:
            visited[nxt] = True
            K = nxt
            count += 1
            break
    else:
        break

print(count, K)
