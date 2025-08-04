N = int(input())
coins = list(map(int, input().split()))
max_sum = now = coins[0]

for c in coins[1:]:
    now = max(c, now + c)
    max_sum = max(max_sum, now)

print(max(max_sum, 0))
