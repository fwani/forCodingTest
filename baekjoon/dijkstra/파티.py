# N 학생수 (=마을수)
# X 번 마을 (1 <= X <= N)
# M 단방향 도로
# i번째 길을 지나는데 시간 Ti(1 <= Ti <= 100)
import sys

# input
# N M X
# s e Ti (* M)

N, M, X = map(int, sys.stdin.readline().strip().split())

graph = {i: [] for i in range(N)}
dist = {i: -1 for i in range(N)}

for _ in range(M):
    s, e, ti = map(int, sys.stdin.readline().strip().split())
