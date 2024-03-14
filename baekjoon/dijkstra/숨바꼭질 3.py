# N (0 <= N <= 100,000)
# K (0 <= K <= 100,000)
# 걷기 1초 X-1 or X+1
# 순간이동 0초 X*2
import sys
from collections import deque


def find(x):
    q = deque()
    q.append(x)
    check[x] = True
    dist[x] = 0

    while q:
        now = q.popleft()
        if now == K:
            return
        if 0 < now * 2 < LIMIT and not check[now * 2]:
            q.appendleft(now * 2)
            check[now * 2] = True
            dist[now * 2] = dist[now]
        if 0 <= now + 1 < LIMIT and not check[now + 1]:
            q.append(now + 1)
            check[now + 1] = True
            dist[now + 1] = dist[now] + 1
        if 0 <= now - 1 < LIMIT and not check[now - 1]:
            q.append(now - 1)
            check[now - 1] = True
            dist[now - 1] = dist[now] + 1


N, K = map(int, sys.stdin.readline().strip().split())

LIMIT = 100001
dist = [-1 for _ in range(LIMIT)]
check = [False for _ in range(LIMIT)]

find(N)
print(dist[K])
