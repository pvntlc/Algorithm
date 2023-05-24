#10423번 : 전기가 부족해 – Gold 2
import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
"""

"""

def find_parent(x):
    if parent[x] < 0:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union(x,y):
    px = find_parent(x)
    py = find_parent(y)

    if px == py:
        return True

    if parent[px] < parent[py]:
        parent[px] += parent[py]
        parent[py] = px
    else:
        parent[py] += parent[px]
        parent[px] = py
    return False

def kruskal(n, edge):
    cost = 0
    cnt = 0
    for u, v, w in edge:
        if union(u, v):
            continue
        cost += w
        cnt += 1

        if cnt == n - 1:
            return cost

    return 0

n, m, k = map(int, input().split())
k_list = list(map(int, input().split()))
parent = [-1] * (n+1)
parent[0] = -k

for i in k_list:
    parent[i] = 0

n_list = [list(map(int, input().split())) for _ in range(m)]
n_list.sort(key=lambda x : x[2])
print(kruskal(n - k + 1, n_list))