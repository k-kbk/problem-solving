n, t = input().split(" ")
n = int(n)

games = {"Y": 2, "F": 3, "O": 4}

players = set()

for _ in range(n):
    players.add(input())

print(int(len(players) / (games[t] - 1)))
