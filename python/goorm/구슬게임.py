N, M, K = map(int, input().split())
dp = [[0 for _ in range(N + M + 1)] for _ in range(K + 1)]
dp[0][N] = 1

for t in range(K):
    for i in range(1, N + M):
        dp[t + 1][i - 1] += dp[t][i]
        dp[t + 1][i] += dp[t][i]
        dp[t + 1][i + 1] += dp[t][i]

answer = 0
for t in range(1, K + 1):
    answer += dp[t][0] + dp[t][N + M]

print(answer)
