def solution(n, words):
    used = set()

    for i, word in enumerate(words):
        if len(word) == 1 or (i > 0 and words[i - 1][-1] != word[0]) or word in used:
            person = i % n + 1
            turn = i // n + 1
            return [person, turn]
        used.add(word)

    return [0, 0]
