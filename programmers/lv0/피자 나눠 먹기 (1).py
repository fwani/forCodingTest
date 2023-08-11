# https://school.programmers.co.kr/learn/courses/30/lessons/120814
from math import ceil


def solution(n):
    return ceil(n / 7)


print(solution(7))  # 1
print(solution(1))  # 1
print(solution(15))  # 3
