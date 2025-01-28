import sys

P = int(sys.stdin.readline())

for _ in range(P):
    cases = list(map(int, sys.stdin.readline().strip().split(" ")))

    T = cases[0]
    students = cases[1:]
    steps = 0
    line = []

    for student in students:
        position = 0

        while position < len(line) and line[position] < student:
            position += 1

        line.insert(position, student)
        steps += len(line) - position - 1

    print(T, steps)
