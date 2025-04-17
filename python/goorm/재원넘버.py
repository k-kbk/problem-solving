# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

input = sys.stdin.readline

n = int(input().rstrip())

dp = [0] * (n + 1)
dp[1] = 3

if n == 1:
	print(dp[1])
else:
	for i in range(2, n + 1):
		dp[i] = (dp[i - 1] + 1) * 3
	print(dp[n])
