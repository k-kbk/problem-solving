import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)


def bfs(start, graph, visited):
    q = deque([start])
    while q:
        current = q.popleft()
        for node in graph[current]:
            if not visited[node] and current in graph[node]:
                q.append(node)
                visited[node] = True


visited = [False] * (n + 1)
count = 0

for i in range(1, n + 1):
    if not visited[i]:
        bfs(i, graph, visited)
        count += 1

print(count)
