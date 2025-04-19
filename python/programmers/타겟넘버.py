def solution(numbers, target):
    answer = 0
    bfs = [0]

    for num in numbers:
        temp = []
        for n in bfs:
            temp.append(n - num)
            temp.append(n + num)
        bfs = temp

    for n in bfs:
        if n == target:
            answer += 1
            
    return answer
