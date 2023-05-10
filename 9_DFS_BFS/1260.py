# 1260번 : DFS와 BFS – Silver 2
import sys
from collections import deque
input = sys.stdin.readline

"""

"""
result = []
def dfs(n_list, visited, v):
    result.append(v)
    visited[v] = True
    for w in sorted(n_list[v]):
        if not visited[w]:
            dfs(n_list, visited, w)

def bfs(n_list, visited, v):
    result = []
    visited[v] = True
    que = deque()
    que.append(v)
    while que:
        node = que.popleft()
        result.append(node)
        for w in sorted(n_list[node]):
            if not visited[w]:
                que.append(w)
                visited[w] = True
    return result

def solution():
    n, m, v = map(int, input().split())
    n_list = [[] for _ in range(n+1)]
    visited = [False] * (n+1)

    for _ in range(m):
        a,b = map(int, input().split())
        n_list[a].append(b)
        n_list[b].append(a)
    dfs(n_list, visited, v)
    print(' '.join(map(str, result)))
    visited = [False] * (n + 1)
    print(' '.join(map(str, bfs(n_list, visited, v))))

solution()