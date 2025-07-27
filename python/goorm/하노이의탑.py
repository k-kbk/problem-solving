import sys

sys.setrecursionlimit(10**6)

count = 0
done = False
rods = {1: list(range(20, 0, -1)), 2: [], 3: []}


def hanoi(n, src, aux, dst):
    global count, done

    if n == 0 or done:
        return
    hanoi(n - 1, src, dst, aux)
    if done:
        return
    disk = rods[src].pop()
    rods[dst].append(disk)
    count += 1
    if count == K:
        done = True
        return
    hanoi(n - 1, aux, src, dst)


K = int(input())
hanoi(20, 1, 2, 3)

print(*[sum(rods[i]) for i in [1, 2, 3]])
