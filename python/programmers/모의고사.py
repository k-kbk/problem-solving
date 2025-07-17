def solution(answers):
    patterns = {
        1: [1, 2, 3, 4, 5],
        2: [2, 1, 2, 3, 2, 4, 2, 5],
        3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    }
    scores = {1: 0, 2: 0, 3: 0}
    for i, answer in enumerate(answers):
        for person, pattern in patterns.items():
            if pattern[i % len(pattern)] == answer:
                scores[person] += 1
    max_score = max(scores.values())
    result = [person for person, score in scores.items() if score == max_score]

    return sorted(result)
