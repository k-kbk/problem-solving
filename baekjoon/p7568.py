n = int(input())

people = list()
answer = list()

for _ in range(n):
    data = list(map(int, input().split()))
    people.append(data)

for i in range(n):
    count = 0

    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            count += 1

    answer.append(count + 1)

for d in answer:
    print(d, end=" ")
