# https://school.programmers.co.kr/learn/courses/30/lessons/120815
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a * b / gcd(a, b)


def solution(n):
    return int(lcm(n, 6) / 6)


print(solution(6))  # 1
print(solution(10))  # 5
print(solution(4))  # 2
