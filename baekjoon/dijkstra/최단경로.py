# V 정점 개수 (1 <= V <= 20,000)
# E 간선 개수 (1 <= E <= 300,000)
# K 시작점
# (u, v, w) u->v 가는 가중치 w, u!=v
import heapq
import sys


def get_min_node():
    node = 1
    minimum = INF
    for k, v in distance.items():
        if visited[k]:
            continue
        if v < minimum:
            node = k
    return node


def dijkstra(start):  # 시간 초과
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]

    for _ in range(V - 1):
        now = get_min_node()
        visited[now] = True
        for i in graph[now]:
            cost = i[1] + distance[now]  # now 를 거쳐서 가는 cost
            if cost < distance[i[0]]:
                distance[i[0]] = cost


def dijkstra2(start):  # 통과
    heap = []
    heapq.heappush(heap, (0, start))  # dist, node
    distance[start] = 0

    while heap:
        dist, node = heapq.heappop(heap)
        if distance[node] < dist:
            continue

        for i in graph[node]:
            cost = dist + i[1]  # w
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))


V, E = map(int, sys.stdin.readline().strip().split())
K = int(sys.stdin.readline().strip())

graph = {i: [] for i in range(1, V + 1)}
visited = {i: False for i in range(1, V + 1)}
INF = sys.maxsize
distance = {i: INF for i in range(1, V + 1)}

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    graph[u].append((v, w))

dijkstra(K)

for v in distance.values():
    print(v if v != INF else "INF")
