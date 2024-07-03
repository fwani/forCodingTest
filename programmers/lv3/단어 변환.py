def check_diff_one(a, b):
    diff_cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff_cnt += 1
        if diff_cnt > 1:
            break
    return diff_cnt == 1


def solution(begin, target, words):
    if target not in words:
        return 0

    global answer
    answer = len(words)
    visited = [False] * len(words)

    def dfs(current, step):
        global answer
        if step >= answer:
            return
        if current == target:
            answer = min(answer, step)
            return
        for i, word in enumerate(words):
            if not visited[i] and check_diff_one(current, word):
                visited[i] = True
                dfs(word, step + 1)
                visited[i] = False

    dfs(begin, 0)
    return answer


assert solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 4
assert solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
