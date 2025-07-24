import sys

input = sys.stdin.readline
N = int(input())
H = list(map(int, input().split()))

total_attacks = 0

for hp in H:
    cycle = hp // 10
    attacks_used = cycle * 4
    hp -= cycle * 10
    total_attacks += attacks_used

    while hp > 0:
        hp -= (total_attacks % 4) + 1
        total_attacks += 1

print(total_attacks)
