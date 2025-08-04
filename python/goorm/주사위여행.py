N, M, K = map(int, input().split())
matrix = [[0] * M for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    matrix[r - 1][c - 1] = 1

dp = [[0] * M for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(M):
        for k in range(1, 7):
            if i - k >= 0 and not matrix[i - k][j]:
                dp[i][j] += dp[i - k][j]
                dp[i][j] %= 10**9 + 7
            if j - k >= 0 and not matrix[i][j - k]:
                dp[i][j] += dp[i][j - k]
                dp[i][j] %= 10**9 + 7

print(dp[N - 1][M - 1])
