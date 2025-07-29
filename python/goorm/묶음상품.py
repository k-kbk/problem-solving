def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x == root_y:
        return False
    parent[root_y] = root_x
    return True


def count_bundles(n, operations):
    parent = [i for i in range(n + 1)]
    count = n

    for a, b in operations:
        if union(parent, a, b):
            count -= 1

    return count


N, M = map(int, input().split())
bundles = [list(map(int, input().split())) for _ in range(M)]
print(count_bundles(N, bundles))
