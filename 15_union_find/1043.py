#1043번 : 거짓말 – Gold 4
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
    parent[x] = find_parent(parent[x])
    return parent[x]

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

def count_liar_party(party):
    count = 0
    for i in party:
        if find_parent(i) != find_parent(0):
            count += 1
    return count

n, m = map(int, input().split())
parent = [-1] * (n+1)
party = []

for i in map(int, input().split()[1:]):
    union(i,0)

for _ in range(m):
    n_list = list(map(int, input().split()))
    party.append(n_list[1])
    for i in range(2, n_list[0]+1):
        union(n_list[i], n_list[1])

print(count_liar_party(party))