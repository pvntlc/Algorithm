#1368번 : 물대기 - Gold 2
import sys
import heapq as hq
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
INF = 10**5 + 1
"""

"""
def prim(size, start, graph):
    total = 0
    pq = []
    visited = [False] * size
    dist = [INF] * size

    dist[start] = 0
    hq.heappush(pq, (0,start))

    while pq:
        cost, curr = hq.heappop(pq)

        if visited[curr]:
            continue

        visited[curr] = True
        total += cost

        for i in range(size):
            if not visited[i] and graph[curr][i] < dist[i]:
                dist[i] = graph[curr][i]
                hq.heappush(pq, (graph[curr][i], i))
    return total

n = int(input())
cost = [int(input()) for _ in range(n)]

# 논들 사이에서 물을 끌어오는 비용
graph = [list(map(int, input().split())) for _ in range(n)]

# 수원지로부터 물을 끌어오는 비용
graph.append(cost + [0])
for i in range(n):
    graph[i].append(cost[i])

# 연산 & 출력
print(prim(n+1, n, graph))