def solution(people, limit):
    people.sort()
    light, heavy = 0, len(people) - 1
    boats = 0
    while light <= heavy:
        if people[light] + people[heavy] <= limit:
            light += 1
        heavy -= 1
        boats += 1
    
    return boats
