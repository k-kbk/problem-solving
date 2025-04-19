import sys

input = sys.stdin.readline

print(max(map(eval, input().rstrip().split())))
