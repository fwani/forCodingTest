# https://school.programmers.co.kr/learn/courses/30/lessons/120923

def solution(num, total):
    start = total // num - (num - 1) // 2
    return list(range(start, start + num))


print(solution(3, 12))  # [3, 4, 5]
print(solution(4, 14))  # [2, 3, 4, 5]
print(solution(5, 5))  # [-1, 0, 1, 2, 3]
