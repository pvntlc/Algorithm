# 2252번 : 줄 세우기 - Gold 3
import sys
from collections import deque
input = sys.stdin.readline
"""

"""
def solution():
    n,m = map(int, input().split())
    n_list = [[] for _ in range(n+1)]
    inDegree = [0] * (n+1)
    que = deque()
    answer = []

    for _ in range(m):
        a,b = map(int, input().split())
        n_list[a].append(b)
        inDegree[b] += 1

    for i in range(1, n+1):
        if inDegree[i] == 0:
            que.append(i)

    while que:
        node = que.popleft()
        answer.append(node)
        for i in n_list[node]:
            inDegree[i] -= 1
            if inDegree[i] == 0:
                que.append(i)

    print(*answer)
solution()