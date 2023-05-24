# 2252번 : 줄 세우기 - Gold 3
import sys
from collections import deque
input = sys.stdin.readline
"""

"""
T = int(input())

def solution():
    n,m = map(int, input().split())
    n_list = [[] for _ in range(n+1)]
    inDegree = [0] * (n+1)
    que = deque()
    answer = []
    Time = [0] + list(map(int, input().split()))
    DP = [0 for _ in range(n+1)]

    for _ in range(m):
        a,b = map(int, input().split())
        n_list[a].append(b)
        inDegree[b] += 1

    for i in range(1, n+1):
        if inDegree[i] == 0:
            que.append(i)
            DP[i] += Time[i]
    final_node = int(input())

    while que:
        node = que.popleft()
        if node == final_node:
            break
        for i in n_list[node]:
            inDegree[i] -= 1
            DP[i] = max(DP[node] + Time[i], DP[i])
            if inDegree[i] == 0:
                que.append(i)


    print(DP[final_node])

for _ in range(T):
    solution()