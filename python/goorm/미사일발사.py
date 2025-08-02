import sys

input = sys.stdin.readline

N = int(input())
events = []
distance = []

for _ in range(N):
    X, Y, T = map(int, input().split())
    d = 2 * (X**2 + Y**2)
    distance.append(d)
    events.append((T, 1))
    events.append((T + d, -1))

events.sort()
now = 0
max_count = 0

for t, e in events:
    now += e
    if now > max_count:
        max_count = now

print(sum(distance) - max_count)
