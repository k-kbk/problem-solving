N = int(input())
A = list(map(int, input().split()))

diff_sum = sum(abs(A[i] - A[i - 1]) for i in range(1, N))
result = (N * 2) + A[0] + A[-1] + diff_sum

print(result)
