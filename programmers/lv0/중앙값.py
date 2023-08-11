# https://school.programmers.co.kr/learn/courses/30/lessons/120811

def solution(array):
    sorted_array = sorted(array)
    return sorted_array[len(sorted_array) // 2]


print(solution([1, 2, 7, 10, 11]))  # 7
print(solution([9, -1, 0]))  # 0
