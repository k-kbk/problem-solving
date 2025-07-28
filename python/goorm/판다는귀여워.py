N, M, K = map(int, input().split())
pandas = [tuple(map(int, input().split())) for _ in range(K)]

answer = float("inf")

for r in range(1, N + 1):
    for c in range(1, M + 1):
        if (r, c) in pandas:
            continue
        acc = 0
        for p_r, p_c in pandas:
            acc += (r - p_r) ** 2 + (c - p_c) ** 2
        answer = min(answer, acc)

print(answer)
