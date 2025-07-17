import sys

input = sys.stdin.readline

n = int(input().rstrip())
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))

for i in range(n):
    count = 0
    for j in range(n):
        if a[i] < a[j] and b[i] < b[j]:
            count += 1
    print(count, end=" ")
