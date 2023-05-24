# 18116번 : 로봇 조립 - Gold 4
import sys
input = sys.stdin.readline

'''
https://www.acmicpc.net/problem/18116

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
parent = [-1] * (1000001)

for _ in range(n):
    line = list(input().split())
    if line[0] == "I":
        union(int(line[1]), int(line[2]))
    elif line[0] == "Q":
        print(-parent[find_parent(int(line[1]))])