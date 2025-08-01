from collections import deque

N, M = map(int, input().split())
graph = [list(input()) for _ in range(M)]
visited = [[False] * N for _ in range(M)]
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
count = 0
biggest = 0

for i in range(M):
    for j in range(N):
        if visited[i][j] or graph[i][j] == ".":
            continue
        visited[i][j] = True
        q = deque([(i, j)])
        size = 1
        while q:
            r, c = q.popleft()
            for d_r, d_c in directions:
                new_r, new_c = d_r + r, d_c + c
                if (
                    0 <= new_r < M
                    and 0 <= new_c < N
                    and not visited[new_r][new_c]
                    and graph[new_r][new_c] == "#"
                ):
                    visited[new_r][new_c] = True
                    q.append((new_r, new_c))
                    size += 1
        count += 1
        biggest = max(biggest, size)

print(count)
print(biggest)
