from collections import defaultdict

def solution(genres, plays):
    genre_total = defaultdict(int)
    genre_songs = defaultdict(list)
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_total[g] += p
        genre_songs[g].append((p, i))
    
    sorted_genres = sorted(genre_total.items(), key=lambda x: -x[1])
    
    answer = list()
    for genre, _ in sorted_genres:
        songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        answer += [i for _, i in songs[:2]]
    
    return answer
