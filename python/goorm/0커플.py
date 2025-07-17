N = int(input())
S = list(map(int, input().split()))
s_set = set(S)

print(sum(x for x in s_set if -x not in s_set))
