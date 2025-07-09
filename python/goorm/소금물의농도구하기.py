# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math

N, M = map(int, input().split())
salt = 0.07 * N
total = N + M
result = (salt / total) * 100
result = math.floor(result * 100) / 100

print(f"{result:.2f}")
