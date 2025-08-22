from math import inf
from heapq import heappop, heappush

N, M = map(int, input().split())
S = [input().strip() for _ in range(N)]

for i in range(N):
    for j in range(M):
        if S[i][j] == "S":
            start_i = i
            start_j = j
        elif S[i][j] == "E":
            end_i = i
            end_j = j

dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
pq = [(0, start_i, start_j, 0)]
dist = [[[inf] * 8 for _ in range(M)] for _ in range(N)]

for k in range(8):
    dist[start_i][start_j][k] = 0

while pq:
    d, i, j, k = heappop(pq)
    if dist[i][j][k] < d:
        continue

    if S[i][j].isdigit():
        next_i = i + dir[k][0]
        next_j = j + dir[k][1]
        if (
            0 <= next_i < N
            and 0 <= next_j < M
            and S[next_i][next_j] != "#"
            and dist[next_i][next_j][k] > dist[i][j][k] + int(S[i][j])
        ):
            dist[next_i][next_j][k] = dist[i][j][k] + int(S[i][j])
            heappush(pq, (dist[next_i][next_j][k], next_i, next_j, k))

    else:
        for nk in range(8):
            next_i = i + dir[nk][0]
            next_j = j + dir[nk][1]
            if (
                0 <= next_i < N
                and 0 <= next_j < M
                and S[next_i][next_j] != "#"
                and dist[next_i][next_j][nk] > dist[i][j][k] + 1
            ):
                dist[next_i][next_j][nk] = dist[i][j][k] + 1
                heappush(pq, (dist[next_i][next_j][nk], next_i, next_j, nk))

res = inf

for k in range(8):
    res = min(res, dist[end_i][end_j][k])

if res < inf:
    print(res)
else:
    print(-1)
