N, K = map(int, input().split())
nums = list(map(int, input().split()))

print(sorted(nums, key=lambda x: (-bin(x).count("1"), -x))[K - 1])
