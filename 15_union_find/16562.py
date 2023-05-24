# 16562번 : 친구비 - Gold 4
import sys
input = sys.stdin.readline

'''
https://www.acmicpc.net/problem/16562

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

    if price[px] < price[py]:
        parent[py] = px
    else:
        parent[px] = py
    return False

n,m,k = map(int, input().split())
price = [0] + list(map(int, input().split()))
parent = [-1] * (n+1)

for _ in range(m):
    x,y = map(int, input().split())
    union(x,y)

sum_price = 0
for i in range(1,n+1):
    if parent[i] == -1:
        sum_price += price[i]
if sum_price > k:
    print("Oh no")
else:
    print(sum_price)