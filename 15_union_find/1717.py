# 1717번 : 집합의 표현 – Gold 4
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
"""
1. 진실을 아는 사람들을 같은 집합으로 묶는다.
2. 파티에 오는 사람들을 검사하고, 진실을 아는 사람들이 있다면 모두 같은 집합으로 묶는다.
3. 만약 아무도 진실을 아는 사람이 없다면 거짓말을 한다.
4. 진실을 아는 사람들을 모두 정리한 후, 다시 검사.
"""
def find_parent(x):
    if parent[x] < 0:
        return x
    return find_parent(parent[x])

def union(x,y):
    px = find_parent(x)
    py = find_parent(y)

    if px == py:
        return

    if parent[px] < parent[py]:
        parent[px] += parent[py]
        parent[py] = px
    else:
        parent[py] += parent[px]
        parent[px] = py
    return

n, m = map(int, input().split())
parent = [-1] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())

    if a == 0:
        union(b,c)
    else:
        if find_parent(b) == find_parent(c):
            print("YES")
        else:
            print("NO")