from math import inf
from collections import deque


def bfs(K):
    dist = [[[inf] * (K + 1) for _ in range(M)] for _ in range(N)]
    dq = deque([(0, 0, K)])
    dist[0][0][K] = 0

    while dq:
        i, j, k = dq.popleft()

        if k < K and grid[i][j] == 2 and dist[i][j][k + 1] > dist[i][j][k] + 1:
            dist[i][j][k + 1] = dist[i][j][k] + 1
            dq.append((i, j, k + 1))

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if not (0 <= ni < N and 0 <= nj < M) or grid[ni][nj] == 0:
                continue
            if grid[i][j] == 2 and grid[ni][nj] == 2:
                if dist[ni][nj][k] > dist[i][j][k] + 1:
                    dist[ni][nj][k] = dist[i][j][k] + 1
                    dq.append((ni, nj, k))
            elif k > 0 and dist[ni][nj][k - 1] > dist[i][j][k] + 1:
                dist[ni][nj][k - 1] = dist[i][j][k] + 1
                dq.append((ni, nj, k - 1))

    return any(dist[N - 1][M - 1][k] <= T for k in range(K + 1))


N, M, T = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
l, r, ans = 0, N * M - 1, -1

while l <= r:
    mid = (l + r) // 2
    if bfs(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

print(ans)
