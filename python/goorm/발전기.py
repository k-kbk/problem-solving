import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
village = [list(map(int, input().split())) for _ in range(n)]


def dfs(start, visited):
    stack = deque([start])
    while stack:
        y, x = stack.popleft()
        visited[y][x] = True
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_y = y + dy
            next_x = x + dx
            if 0 <= next_y < n and 0 <= next_x < n:
                if village[next_y][next_x] and not visited[next_y][next_x]:
                    stack.appendleft((next_y, next_x))


visited = [[False] * n for _ in range(n)]
count = 0

for i in range(n):
    for j in range(n):
        if village[i][j] and not visited[i][j]:
            dfs((i, j), visited)
            count += 1

print(count)
