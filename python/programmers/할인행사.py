from collections import Counter

def solution(want, number, discount):
    d = sorted(list(zip(want, number)))
    count = 0
    
    for i in range(len(discount) - 9):
        counter = sorted(list(Counter(discount[i:i + 10]).items()))
        if d == counter:
            count += 1
    
    return count
