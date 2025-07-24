N, M, X = map(int, input().split())
H = list(map(int, input().split()))
Q = int(input())
D = list(input().split())

answer = 0
count = 0

for move in D:
    idx = X - 1
    height = H[idx] + count
    if height >= M:
        answer += height
        H[idx] = -count
    count += 1

    if move == "L":
        X = (X - 2) % N + 1
    elif move == "R":
        X = X % N + 1

print(answer)
