from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(start_x, start_y):
    queue = deque([[start_x, start_y]])
    arr[start_x][start_y] = 0
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if arr[nx][ny] == 1:
                queue.append([nx, ny])
                arr[nx][ny] = 0


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * n for _ in range(m)]
    for _ in range(k):
        a, b = map(int, input().split())
        arr[a][b] = 1

    count = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)
