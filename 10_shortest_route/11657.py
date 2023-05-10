#11657번 : 타임머신 – Gold 4
import sys
import heapq as hq
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int, input().split())
n_list = [tuple(map(int, input().split())) for _ in range(m)]
graph = [INF] * (n+1)

def bellman_ford(start):
    graph[start] = 0

    for i in range(1, n+1):
        for j in range(m):
            now, next, cost = n_list[j][0], n_list[j][1], n_list[j][2]
            if graph[now] != INF and graph[next] > graph[now] + cost:
                graph[next] = graph[now]+cost
                if i == n:
                    return True
    return False

if bellman_ford(1):
    print(-1)
else:
    for i in range(2, n+1):
        print(graph[i] if graph[i] != INF else -1)