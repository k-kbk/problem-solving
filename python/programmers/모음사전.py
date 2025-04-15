from itertools import product

def solution(word):
    aeiou = ['A', 'E', 'I', 'O', 'U']
    dictionary = []
    for i in range(1, 6):
        for comb in product(aeiou, repeat=i):
            dictionary.append(''.join(comb))
    dictionary.sort()

    return dictionary.index(word) + 1
