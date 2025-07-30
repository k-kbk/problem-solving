from bisect import bisect_right

N = int(input())
S = list(map(int, input().split()))
S.sort()

count = 0

for i in range(N):
    for j in range(i + 1, N):
        limit = S[i] + S[j]
        k = bisect_right(S, limit)
        count += max(0, k - (j + 1))

print(count)
