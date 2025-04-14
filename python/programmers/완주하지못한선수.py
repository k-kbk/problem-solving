from collections import Counter

def solution(participant, completion):
    pc = Counter(participant)
    cc = Counter(completion)
    answer = pc - cc
    
    return list(answer.keys())[0]
