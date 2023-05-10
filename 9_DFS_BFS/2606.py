# 2606번 : 바이러스 - Silver 3
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
"""

"""
def bfs_virus(v):
    que = deque()
    que.append(v)
    result = []
    visited[v] = True

    while que:
        node = que.popleft()
        result.append(node)
        for w in n_list[node]:
            if visited[w] == False:
                que.append(w)
                visited[w] = True
    return result

n = int(input())
m = int(input())

n_list = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    a,b = map(int, input().split())
    n_list[a].append(b)
    n_list[b].append(a)
print(len(bfs_virus(1))-1)