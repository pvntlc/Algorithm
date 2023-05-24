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
        return

    if parent[px] > parent[py]:
        parent[py] += parent[px]
        parent[px] = py
    else:
        parent[px] += parent[py]
        parent[py] = px
    return
T = int(input())
for _ in range(T):
    f = int(input())
    parent = [-1] * (2*f)
    f_dict = dict()
    idx = 0
    for _ in range(f):
        name1, name2 = input().split()

        if not name1 in f_dict:
            f_dict[name1] = idx
            idx += 1

        if not name2 in f_dict:
            f_dict[name2] = idx
            idx += 1

        union(f_dict[name1], f_dict[name2])
        print(-parent[find_parent(f_dict[name1])])