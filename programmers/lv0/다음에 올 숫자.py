# https://school.programmers.co.kr/learn/courses/30/lessons/120924

def solution(common):
    # 등차수열
    if common[1] - common[0] == common[2] - common[1]:
        return common[-1] + common[1] - common[0]
    # 등비수열
    else:
        return common[-1] * (common[1] // common[0])


print(solution([1, 2, 3, 4]))  # 5
print(solution([2, 4, 8]))  # 16
