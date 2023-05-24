import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
parent = [[-1,i] for i in map(int, ("0 "+ input()).split())]

def find_parent(x):
    if parent[x][0] < 0:
        return x
    parent[x][0] = find_parent(parent[x][0])
    return parent[x][0]

def union(x,y):
    px = find_parent(x)
    py = find_parent(y)

    if px == py:
        return

    if parent[px][0] > parent[py][0]:
        parent[py][0] += parent[px][0]
        parent[py][1] += parent[px][1]
        parent[px][0] = py
    else:
        parent[px][0] += parent[py][0]
        parent[px][1] += parent[py][1]
        parent[py][0] = px

    return

def knapsack(k):
    dp = [0] * k
    count = []
    for p,c in parent:
        if p<0:
            count.append((-p,c))
    for child, candy in count:
        for i in range(k-1, child-1, -1):
            dp[i] = max(dp[i], dp[i-child] + candy)

    return dp[-1]

for _ in range(m):
    x,y = map(int, input().split())
    union(x,y)
print(knapsack(k))