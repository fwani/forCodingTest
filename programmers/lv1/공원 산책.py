# https://school.programmers.co.kr/learn/courses/30/lessons/172928

def move(park, now, direction, distance):
    next_row, next_col = now
    for _ in range(distance):
        if direction == 'E' and next_col + 1 < len(park[0]):
            next_col = next_col + 1
        elif direction == 'W' and next_col - 1 >= 0:
            next_col = next_col - 1
        elif direction == 'S' and next_row + 1 < len(park):
            next_row = next_row + 1
        elif direction == 'N' and next_row - 1 >= 0:
            next_row = next_row - 1
        else:
            return now
        if park[next_row][next_col] == 'X':
            return now
    return next_row, next_col


def find_start(park):
    for y, row in enumerate(park):
        for x, data in enumerate(row):
            if data == 'S':
                return y, x


def solution(park, routes):
    now = find_start(park)

    for route in routes:
        direction, distance = route.split(" ")
        now = move(park, now, direction, int(distance))
    return list(now)


print(solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"]))  # [2,1]
print(solution(["SOO", "OXX", "OOO"], ["E 2", "S 2", "W 1"]))  # [0,1]
print(solution(["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"]))  # [0,0]
