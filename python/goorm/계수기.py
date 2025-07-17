import sys

input = sys.stdin.readline

n = int(input().rstrip())
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
k = int(input().rstrip())

i = len(b) - 1

while i >= 0 and k > 0:
    sum = k + b[i]
    div = a[i] + 1
    k = sum // div
    b[i] = sum % div
    i -= 1

print("".join(map(str, b)))
