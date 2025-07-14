# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N, K = map(int, input().split())
nums = list(map(int, input().split()))

print(sorted(nums, key=lambda x: (-bin(x).count('1'), -x))[K - 1])
