import math

H, W, N, M = map(int, input().split())

x = math.ceil(W / (M + 1))
y = math.ceil(H / (N + 1))

print(x * y)
