A, B, C = map(int, input().split())
N = int(input())
c_x, c_y = [], []

for _ in range(N):
    c, t = map(int, input().split())
    (c_x if t == 0 else c_y).append(c)

c_x.sort()
c_y.sort()

x, y = min(A, len(c_x)), min(B, len(c_y))
used = c_x[:x] + c_y[:y]
remain = c_x[x:] + c_y[y:]
remain.sort()
z = min(C, len(remain))
ans = used + remain[:z]

print(len(ans), sum(ans))
