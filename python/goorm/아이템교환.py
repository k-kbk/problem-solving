import sys

input = sys.stdin.readline

N, M = map(int, input().split())

goorm = set(input().split())
friend = set(input().split())

for _ in range(M):
    a, b = input().split()
    if a in goorm and b in friend:
        goorm.remove(a)
        friend.remove(b)
        goorm.add(b)
        friend.add(a)

print(*sorted(goorm))
