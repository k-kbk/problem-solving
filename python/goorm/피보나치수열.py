N = int(input())

dp = [0] * N
dp[1] = 1
dp[2] = 1

if N <= 2:
    print(N - 1)
else:
    for i in range(2, N):
        dp[i] = (dp[i - 1] + dp[i - 2]) % (10**9 + 7)

print(dp[N - 1])
