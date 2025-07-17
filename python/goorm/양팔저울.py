def dfs(i, sum):
    if i == k:
        if 0 < sum <= max_value:
            result.add(sum)
    else:
        dfs(i + 1, sum + g_list[i])
        dfs(i + 1, sum - g_list[i])
        dfs(i + 1, sum)


k = int(input())
g_list = list(map(int, input().split()))
max_value = sum(g_list)
result = set()
dfs(0, 0)

print(max_value - len(result))
