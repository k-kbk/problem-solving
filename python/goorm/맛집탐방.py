from collections import defaultdict, deque

N = int(input())
graph = defaultdict(list)

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(start):
    visited = {start}
    q = deque([(start, 0)])
    far_node, max_dist = start, 0
    while q:
        node, dist = q.popleft()
        if dist > max_dist:
            far_node, max_dist = node, dist
        for r in graph[node]:
            if r not in visited:
                visited.add(r)
                q.append((r, dist + 1))
    return far_node, max_dist


if N == 1:
    print(1)
else:
    u, _ = bfs(1)
    _, d = bfs(u)
    print(d + 1)
