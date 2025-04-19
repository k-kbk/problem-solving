import sys

input = sys.stdin.readline

def solution(a, b, c, n):
	if n < a:
		return 0
		
	dp = [0] * 301
	dp[a] = 1
	dp[b] = 1
	dp[c] = 1

	for i in range(a + 1, n + 1):
		dp[i] = int(dp[i - a] or dp[i - b] or dp[i - c])

	return dp[n]

a, b, c, n = map(int, input().rstrip().split())

print(solution(a, b, c, n))
