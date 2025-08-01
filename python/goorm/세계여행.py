from collections import deque


def bfs(lang):
    q = deque([1])
    visited = [False] * (N + 1)
    visited[1] = True

    while q:
        now = q.popleft()
        for n in G[now]:
            if not visited[n] and (a[n] == a[1] or a[n] == lang):
                visited[n] = True
                q.append(n)

    return sum(visited)


N, M = map(int, input().split())
a = [0] + list(map(int, input().split()))

G = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

ans = 0
for lang in range(1, 11):
    if lang != a[1]:
        ans = max(ans, bfs(lang))

print(ans)
