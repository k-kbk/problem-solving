import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))

arr = [list(map(int, input().split(" "))) for _ in range(N)]

direction = [-1, 0, 1]


def dfs(row, col, dir, low, answer):
    if row == N - 1:
        return min(low, answer)

    for i in direction:
        if i != dir:
            if 0 <= row + 1 < N and 0 <= col + i < M:
                low = dfs(row + 1, col + i, i, low, answer + arr[row + 1][col + i])

    return low


low = int(sys.maxsize)

for i in range(M):
    low = min(dfs(0, i, 2, low, arr[0][i]), low)

print(low)
