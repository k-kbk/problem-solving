# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def solve(n, d, p):
    p.sort()
    left = 0
    distance = 0
    for right in range(n):
        while p[right] - p[left] > d:
            left += 1
        distance = max(distance, right - left + 1)

    return n - distance

N, D = map(int, input().split())
P = list(map(int, input().split()))
print(solve(N, D, P))
