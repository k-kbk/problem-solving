from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(sx, sy, ex, ey):
    dist = [[-1] * N for _ in range(N)]
    dist[sy][sx] = 0
    dq = deque()
    dq.append((sy, sx))

    while dq:
        y, x = dq.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and dist[ny][nx] == -1 and not A[ny][nx]:
                dist[ny][nx] = dist[y][x] + 1
                dq.append((ny, nx))

    return dist[ey][ex]


N, M = map(int, input().split())
X, Y, Z = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
a, b, c, d = [], [], [], []

for _ in range(M):
    ai, bi, ci, di = map(int, input().split())
    a.append(ai)
    b.append(bi)
    c.append(ci)
    d.append(di)

x, y = a[0] - 1, b[0] - 1
res = 0

for i in range(M):
    move = bfs(x, y, a[i] - 1, b[i] - 1)
    work = bfs(a[i] - 1, b[i] - 1, c[i] - 1, d[i] - 1)
    x, y = c[i] - 1, d[i] - 1

    res += X if work <= 5 else X + (work - 5) * Y
    res -= (move + work) * Z

print(res)
