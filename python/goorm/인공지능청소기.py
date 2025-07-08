import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    X, Y, N = map(int, input().split())
    distance = abs(X) + abs(Y)
    print("YES" if distance <= N and (N - distance) % 2 == 0 else "NO")
