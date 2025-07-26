N = int(input())
islands = [(*map(int, input().split()), i) for i in range(N)]
islands.sort(key=lambda x: (x[0], x[1]))
answer = [0] * N

for i, (_, _, idx) in enumerate(islands):
    answer[idx] = N - i - 1

print(*answer, sep="\n")
