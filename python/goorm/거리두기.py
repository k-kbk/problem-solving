MOD = 100_000_007
N = int(input())
dp = [[0] * 5 for _ in range(N)]

for i in range(5):
    dp[0][i] = 1

for i in range(1, N):
    dp[i][0] = (
        dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4]
    ) % MOD
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2] + dp[i - 1][3]) % MOD
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][4]) % MOD
    dp[i][3] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % MOD
    dp[i][4] = (dp[i - 1][0] + dp[i - 1][2]) % MOD

print(sum(dp[N - 1]) % MOD)
