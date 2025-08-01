from collections import deque


R, C = map(int, input().split())
S = [input() for _ in range(R)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dist = [[0] * C for _ in range(R)]
visited = [[False] * C for _ in range(R)]
q = deque()

for i in range(R):
    for j in range(C):
        if S[i][j] == "@":
            q.append((i, j))
            visited[i][j] = True

while q:
    i, j = q.popleft()
    for d_i, d_j in directions:
        n_i, n_j = i + d_i, j + d_j
        if (
            0 <= n_i < R
            and 0 <= n_j < C
            and S[n_i][n_j] != "#"
            and not visited[n_i][n_j]
        ):
            visited[n_i][n_j] = True
            dist[n_i][n_j] = dist[i][j] + 1
            q.append((n_i, n_j))

for i in range(R):
    for j in range(C):
        if S[i][j] == "&":
            print(-1 if not visited[i][j] else dist[i][j] - 1)
