# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

input = sys.stdin.readline

n = int(input().rstrip())
a, b = map(int, input().rstrip().split())

dp = [float('inf')] * (n + 1)
dp[0] = 0

for i in range(n + 1):
    if i >= a:
        dp[i] = min(dp[i], dp[i - a] + 1)
    if i >= b:
        dp[i] = min(dp[i], dp[i - b] + 1)

print(dp[n] if dp[n] != float('inf') else -1)
