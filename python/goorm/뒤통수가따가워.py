import sys

input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split()))

stack = []
for i in range(N):
    print(len(stack), end=" ")
    while stack and heights[stack[-1]] <= heights[i]:
        stack.pop()
    stack.append(i)
