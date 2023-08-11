# https://school.programmers.co.kr/learn/courses/30/lessons/181832

def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    r = 0
    c = 0
    direction = 'r'
    for i in range(n * n):
        answer[r][c] = i + 1
        if direction == 'r':
            if c + 1 == n or answer[r][c + 1] != 0:
                direction = 'd'
                r += 1
            else:
                c += 1
        elif direction == 'd':
            if r + 1 == n or answer[r + 1][c] != 0:
                direction = 'l'
                c -= 1
            else:
                r += 1
        elif direction == 'l':
            if c - 1 < 0 or answer[r][c - 1] != 0:
                direction = 'u'
                r -= 1
            else:
                c -= 1
        elif direction == 'u':
            if r - 1 < 0 or answer[r - 1][c] != 0:
                direction = 'r'
                c += 1
            else:
                r -= 1
    return answer


print(solution(4))  # [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
print(solution(
    5))  # [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]
