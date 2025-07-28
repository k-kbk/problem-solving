N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
scores = []

for i in range(N):
    for j in range(N):
        if graph[i][j]:
            continue
        clouds = 0
        for r, c in directions:
            if 0 <= i + r < N and 0 <= j + c < N:
                if graph[i + r][j + c]:
                    clouds += 1
        scores.append(clouds)

print(scores.count(K))
