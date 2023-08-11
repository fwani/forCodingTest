# https://school.programmers.co.kr/learn/courses/30/lessons/120813

def solution(n):
    return list(range(1, n + 1, 2))


print(solution(10))  # [1, 3, 5, 7, 9]
print(solution(15))  # [1, 3, 5, 7, 9, 11, 13, 15]
