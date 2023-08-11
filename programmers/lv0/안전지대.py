# https://school.programmers.co.kr/learn/courses/30/lessons/120866

direction = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1)
]


def bfs(board, visited, x, y):
    q = [(x, y)]
    while len(q) > 0:
        a, b = q.pop(0)
        visited[a][b] = True
        for i, j in direction:
            nx = a + i
            ny = b + j
            if 0 <= nx < len(board[0]) and 0 <= ny < len(board) and not visited[nx][ny]:
                if board[nx][ny] == 1:
                    q.append((nx, ny))
                else:
                    board[nx][ny] = 2
    return board


def solution(board):
    visited = [[False] * len(row) for row in board]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                board = bfs(board, visited, i, j)
    answer = 0
    for row in board:
        for data in row:
            if data == 0:
                answer += 1
    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))  # 16
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))  # 13
print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1]]))  # 0
