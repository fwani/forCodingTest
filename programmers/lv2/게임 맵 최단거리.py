import time


def solution(maps):
    max_x = len(maps[0])
    max_y = len(maps)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    max_weight = max_x * max_y + 1
    visited = [[False] * max_x for _ in range(max_y)]
    weight = [[max_weight] * max_x for _ in range(max_y)]

    def bfs(x, y):
        if (x, y) == (max_x - 1, max_y - 1) or (weight[y][x] > weight[max_y - 1][max_x - 1]):
            return
        visited[y][x] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or nx >= max_x or 0 > ny or ny >= max_y or maps[ny][nx] == 0 or visited[ny][nx]:  # 벽
                continue
            if weight[ny][nx] == 0 or weight[ny][nx] > weight[y][x] + 1:
                weight[ny][nx] = weight[y][x] + 1
                bfs(nx, ny)
        visited[y][x] = False

    weight[0][0] = 1
    bfs(0, 0)
    answer = weight[max_y - 1][max_x - 1]
    return answer if answer != max_weight else -1


s = time.time()
assert solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]) == 11
assert solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]) == -1
assert solution([[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1]]) == 9
assert solution([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 9
assert solution([[1, 0, 1, 1, 1], [0, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 0, 0], [1, 1, 1, 0, 1]]) == -1
print(time.time() - s)
