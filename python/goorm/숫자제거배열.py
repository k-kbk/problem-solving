N, K = input().split()
nums = input().split()

print(sum(1 for n in nums if K not in n))
