import sys
from collections import deque

input = sys.stdin.readline

print(max(map(eval, input().rstrip().split())))
