# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
scores = [[0] * n for _ in range(n)]
ground = [list(input().rstrip().split()) for _ in range(n)]
bombs = [list(map(int, input().rstrip().split())) for _ in range(k)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for y, x in bombs:
	y -= 1
	x -= 1
	target = ground[y][x]

	if target == '@':
		scores[y][x] += 2
	elif target == '0':
		scores[y][x] += 1

	for dy, dx in directions:
		next_x = x + dx
		next_y = y + dy
		if (next_x < 0 or next_x >= n) or (next_y < 0 or next_y >= n):
			continue
		target = ground[next_y][next_x]
		if target == '@':
			scores[next_y][next_x] += 2
		elif target == 0:
			scores[next_y][next_x] += 1

print(max(item for row in scores for item in row))
