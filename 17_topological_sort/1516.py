#1516번 : 게임 개발 – Gold 3
import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

"""

"""
def t_sort(n, time,indegree, graph):
    que = deque()
    dp = time[:]

    for i in range(1, n+1):
        if indegree[i] == 0:
            que.append(i)

    while que:
        node = que.popleft()
        for next in graph[node]:
            indegree[next] -= 1
            dp[next] = max(dp[next], dp[node] + time[next])
            if indegree[next] == 0:
                que.append(next)
    return dp[1:]

def solution():
    n = int(input())
    time = [0] * (n + 1)
    indegree = [0] * (n + 1)
    graph = [list() for _ in range(n + 1)]

    for i in range(1, n + 1):
        line = list(map(int, input().split()))
        time[i] = line[0]
        indegree[i] = len(line) - 2
        for v in line[1:-1]:
            graph[v].append(i)

    print(*t_sort(n, time, indegree, graph),sep="\n")


solution()