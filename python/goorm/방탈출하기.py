N = int(input())
A = set(map(int, input().split()))
M = int(input())

for _ in range(M):
    print(1 if int(input()) in A else 0)
