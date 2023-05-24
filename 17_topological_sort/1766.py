#1766번 : 문제집 – Gold 2
import sys
from collections import deque
import heapq as hq

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

"""

"""
def t_sort(n,graph,indegree):
    que = []
    answer = []

    for i in range(1,n+1):
        if indegree[i] == 0:
            hq.heappush(que,i)

    while que:
        node = hq.heappop(que)
        answer.append(node)
        for next in graph[node]:
            indegree[next] -= 1
            if indegree[next] == 0:
                hq.heappush(que, next)
    return answer

def solution():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    for _ in range(m):
        a,b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    print(*t_sort(n, graph, indegree))
solution()