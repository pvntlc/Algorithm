#1197번 : 최소 스패닝 트리 - Gold 4
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

v,e = map(int, input().split())
parent = [-1] * (v+1)
n_list = []
for _ in range(e):
    n_list.append(list(map(int, input().split())))

n_list.sort(key = lambda x : x[2])
count = 0
for s,e,weight in n_list:
    if union(s,e):
        continue
    count += weight
print(count)