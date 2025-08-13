N = int(input())
F = list(map(int, input().split()))
Q = int(input())
LR = [tuple(map(int, input().split())) for _ in range(Q)]
cumulative = [0]

for f in F:
    cumulative.append(cumulative[-1] + f)

for l, r in LR:
    print(cumulative[r] - cumulative[l - 1])
