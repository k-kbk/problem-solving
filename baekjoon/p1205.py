N, newScore, P = map(int, input().split())

if N > 0:
    scores = list(map(int, input().split()))
else:
    scores = []

scores.append(newScore)
scores.sort(reverse=True)

rank = scores.index(newScore) + 1

if rank > P or (N == P and scores[-1] == newScore):
    print(-1)
else:
    print(rank)
