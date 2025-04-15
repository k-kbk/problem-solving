from itertools import permutations

def solution(k, dungeons):
    answer = 0
    sequence = list(permutations(dungeons, len(dungeons)))
    for s in sequence:
        energy = k
        count = 0
        for minimum, reduce in s:
            if energy < minimum:
                break
            energy -= reduce
            count += 1
        answer = max(answer, count)
        
    return answer
