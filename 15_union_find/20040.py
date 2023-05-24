import sys
input = sys.stdin.readline

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


n, m,= map(int, input().split())
parent = [-1] * (n)
for i in range(m):
    x,y = map(int, input().split())
    if union(x,y):
        print(i+1)
        break
else:
    print(0)