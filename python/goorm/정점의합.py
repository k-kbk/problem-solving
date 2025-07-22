from collections import deque

N, M, K = map(int, input().split())
S = list(map(int, input().split()))
visited = [False] * (N + 1)
graph = [[] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)

q = deque([K])

while q:
    now = q.popleft()
    visited[now] = True
    for next in graph[now]:
        if not visited[next]:
            q.append(next)

answer = 0

for i, v in enumerate(visited):
    answer += S[i - 1] if v else 0

print(answer)
