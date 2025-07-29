from collections import defaultdict

N = int(input())
totals = defaultdict(int)

for _ in range(N):
    name, amount = input().split()
    totals[name] += int(amount)

for name in sorted(totals.keys()):
    print(name, totals[name])
