#1647번 : 도시분할계획 - Gold 4
import sys
import heapq as hq
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
INF = 10**5 + 1
"""

"""
def find_parent(x):
    if parent[x] < 0 :
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union(x,y):
    px = find_parent(x)
    py = find_parent(y)

    if px == py:
        return True
    if parent[px] > parent[py]:
        parent[py] += parent[px]
        parent[px] = py
    else:
        parent[px] += parent[py]
        parent[py] = px
    return False

def kruskal(n,n_list):
    total = 0
    count = 0
    for x,y,weight in n_list:
        if union(x,y):
            continue
        total += weight
        count += 1
        if count == n-1:
            return total
    return 0
n,m = map(int, input().split())
parent = [-1] * (n+1)
n_list = [tuple(map(int, input().split())) for _ in range(m)]
n_list.sort(key = lambda x: x[2])
print(kruskal(n-1,n_list))