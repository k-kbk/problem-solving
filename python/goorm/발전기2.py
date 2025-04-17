# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
village = [list(map(int, input().rstrip().split())) for _ in range(n)]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[False] * n for _ in range(n)]
count = [0] * 30

for i in range(n):
	for j in range(n):
		if visited[i][j]:
			continue
		type = village[i][j]
		q = deque([(i, j)])
		visited[i][j] = True
		sum = 1
		while q:
			y, x = q.popleft()
			for dy, dx in directions:
				next_y = y + dy
				next_x = x + dx
				if 0 <= next_y < n and 0 <= next_x < n:
					if not visited[next_y][next_x] and village[next_y][next_x] == type:
						q.append((next_y, next_x))
						visited[next_y][next_x] = True
						sum += 1
		if sum >= k:
			count[type - 1] += 1

max_count = 0
answer = 0

for i, value in enumerate(count):
	if value >= max_count:
		max_count = value
		answer = i + 1

print(answer)
