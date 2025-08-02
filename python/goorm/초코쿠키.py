N = int(input())
A = list(map(int, input().split()))
B = sorted((a, i + 1) for i, a in enumerate(A))

for i, (a, idx) in enumerate(B):
    if a - i <= 0:
        print(*range(1, N + 1))
        break
else:
    print(*(idx for _, idx in B))
