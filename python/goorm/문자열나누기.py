from itertools import combinations

N = int(input())
S = input().strip()
cut_positions = combinations(range(1, N), 2)
substrings = set()

for i, j in cut_positions:
    substrings.update([S[:i], S[i:j], S[j:]])

sorted_substrings = sorted(substrings)
answer = 0

for i, j in combinations(range(1, N), 2):
    parts = [S[:i], S[i:j], S[j:]]
    answer = max(answer, sum(sorted_substrings.index(part) + 1 for part in parts))

print(answer)
