N = int(input())

for _ in range(N):
    a = {n: 0 for n in range(4, 0, -1)}
    for n in map(int, input().split()[1:]):
        a[n] += 1
    b = {n: 0 for n in range(4, 0, -1)}
    for n in map(int, input().split()[1:]):
        b[n] += 1
    if a == b:
        print("D")
        continue
    for i in range(4, 0, -1):
        if a[i] > b[i]:
            print("A")
            break
        if a[i] < b[i]:
            print("B")
            break
print()
