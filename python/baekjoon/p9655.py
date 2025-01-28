# DP

N = int(input())

dp = [False for _ in range(N + 1)]

dp[1] = True  # SK

if N >= 2:
    dp[2] = False  # CY

if N >= 3:
    dp[3] = True  # SK
    for i in range(4, N + 1):
        dp[i] = not dp[i - 1] or not dp[i - 3]

print("SK" if dp[N] else "CY")

# 다른 풀이

# N = int(input())

# print("SK" if N % 2 == 1 else "CY")
