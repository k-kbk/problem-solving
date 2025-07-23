N = int(input())
items = [tuple(input().split()) for _ in range(N)]
items = [(name, int(price)) for name, price in items]

max_item = max(items, key=lambda x: x[1])
min_item = min(items, key=lambda x: x[1])

print(max_item[0], max_item[1])
print(min_item[0], min_item[1])
