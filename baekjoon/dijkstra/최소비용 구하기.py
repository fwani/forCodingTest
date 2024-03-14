# N 도시 개수 (1 <= N <= 1,000)
# M 도시간 운행 버스 개수 (1 <= M <= 100,000)
# N
# M
# A -> B, W
# ...
# start end
import heapq
import sys


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))  # dist, node
    distance[start - 1] = 0

    while heap:
        dist, node = heapq.heappop(heap)
        if distance[node - 1] < dist:
            continue

        for i in graph[node]:
            cost = dist + i[1]  # w
            if cost < distance[i[0] - 1]:
                distance[i[0] - 1] = cost
                heapq.heappush(heap, (cost, i[0]))


N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

graph = {i: [] for i in range(1, N + 1)}
INF = sys.maxsize
distance = [INF for _ in range(N)]

for _ in range(M):
    a, b, w = map(int, sys.stdin.readline().strip().split())
    graph[a].append((b, w))

s, e = map(int, sys.stdin.readline().strip().split())

dijkstra(s)

print(distance[e - 1])
