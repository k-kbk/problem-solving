def calc(wins, games):
    return (wins * 100) // games


N, M = map(int, input().split())
current = calc(M, N)

if current >= 99:
    print("X")
else:
    left, right = 1, 10**12
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        new = calc(M + mid, N + mid)
        if new > current:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer if answer != -1 else "X")
