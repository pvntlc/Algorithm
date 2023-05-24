# 1976번 : 여행 가자 - Gold 4
import sys
input = sys.stdin.readline

'''

'''

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
m = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]
parent = [-1] * (n)
for i in range(n):
    for j in range(n):
        if n_list[i][j] == 1:
            union(i,j)
answer_list = list(map(int, input().split()))
idx = find_parent(answer_list[0]-1)
for i in answer_list:
    idx1 = find_parent(i-1)
    if idx != idx1:
        print("NO")
        break
else:
    print("YES")