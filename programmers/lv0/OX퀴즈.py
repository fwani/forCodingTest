# https://school.programmers.co.kr/learn/courses/30/lessons/120907


def solution(quiz):
    answer = []
    for q in quiz:
        exp, result = q.split("=")
        answer.append("O" if eval(exp.strip()) == int(result.strip()) else "X")
    return answer


print(solution(["3 - 4 = -3", "5 + 6 = 11"]))  # ['X', 'O']
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))  # ['O', 'O', 'X', 'O']
