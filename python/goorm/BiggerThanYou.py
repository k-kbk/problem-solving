import sys
from math import inf

input = sys.stdin.readline


def solve(now):
    if now > K:
        global ans
        ans = min(ans, now)
        return
    for i in range(N):
        nxt = now * 10 + A[i]
        if not nxt:
            continue
        solve(nxt)


N = int(input())
A = list(map(int, input().split()))
K = int(input())

ans = inf
solve(0)
print(ans)
