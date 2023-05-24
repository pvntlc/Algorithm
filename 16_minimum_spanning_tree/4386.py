#4386번 : 별자리 만들기 - Gold 3
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

n = int(input())
n_list = []
answer = []
parent = [-1] * (n)

for _ in range(n):
    x, y = map(float, input().split())
    n_list.append([x,y])

for i in range(n):
    for j in range(n):
        if i==j:
            continue
        x1, y1 = n_list[i]
        x2, y2 = n_list[j]
        weight = math.sqrt((x1 - x2)**2 + (y1-y2)**2)
        answer.append([i,j,weight])

answer.sort(key=lambda x : x[2])

count = 0
for s,e,weight in answer:
    if union(s,e):
        continue
    count += weight

print(round(count,2))