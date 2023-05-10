#1753번 : 최단 경로 - Gold 4
import sys
import heapq as hq
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())
k = int(input())
dp = [INF] * (v+1)
heap = []
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b,w = map(int, input().split())
    graph[a].append((w,b))

def Dijkstra(start):
    hq.heappush(heap, (0, start))
    dp[start] = 0

    while heap:
        weight, node = hq.heappop(heap)
        if dp[node] < weight:
            continue

        for new_weight, new_node in graph[node]:
            if dp[new_node] > weight + new_weight:
                dp[new_node] = weight + new_weight
                hq.heappush(heap, (weight+new_weight, new_node))
Dijkstra(k)
for i in range(1,v+1):
    print(dp[i] if dp[i] != INF else "INF")