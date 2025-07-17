def solution(array, commands):
    answer = list()
    for start, end, index in commands:
        answer.append(sorted(array[start - 1 : end])[index - 1])

    return answer
