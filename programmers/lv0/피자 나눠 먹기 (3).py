# https://school.programmers.co.kr/learn/courses/30/lessons/120816

def solution(_slice, n):
    num = n % _slice
    if num == 0:
        return n // _slice
    else:
        return n // _slice + 1


print(solution(7, 10))  # 2
print(solution(4, 12))  # 3
