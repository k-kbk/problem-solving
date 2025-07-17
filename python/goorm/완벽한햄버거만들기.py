import sys

input = sys.stdin.readline

n = int(input().rstrip())
k = list(map(int, input().rstrip().split()))

is_desc = False
prev = k[0]

for taste in k[1:]:
    if is_desc and taste > prev:
        print(0)
        break
    if taste < prev:
        is_desc = True
    prev = taste
else:
    print(sum(k))
