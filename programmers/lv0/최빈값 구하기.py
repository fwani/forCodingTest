# https://school.programmers.co.kr/learn/courses/30/lessons/120812

def solution(array):
    pair = {}
    for i in array:
        if i in pair:
            pair[i] += 1
        else:
            pair[i] = 1

    _max = -1
    _max_cnt = 0
    for k, v in pair.items():
        if _max == -1 or pair[_max] < v:
            _max = k
            _max_cnt = 1
        elif pair[_max] == v:
            _max_cnt += _max_cnt
    return _max if _max_cnt == 1 else -1


print(solution([1, 2, 3, 3, 3, 4]))  # 3
print(solution([1, 1, 2, 2]))  # -1
print(solution([1]))  # 1
