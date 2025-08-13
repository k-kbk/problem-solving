from collections import defaultdict, Counter

N, S = input().split()
N = int(N)
Q = int(input())
cumulative = [defaultdict(int)]

for c in S:
    last = cumulative[-1].copy()
    last[c] += 1
    cumulative.append(last)

for _ in range(Q):
    l, r, M, T = input().split()
    l = int(l)
    r = int(r)
    M = int(M)
    counter = Counter(T)

    if not counter:
        print(0)
        continue

    ans = min(
        (cumulative[r][c] - cumulative[l - 1][c]) // need for c, need in counter.items()
    )
    print(ans)
