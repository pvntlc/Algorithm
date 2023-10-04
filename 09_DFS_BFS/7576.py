# 7576번 : 토마토 – Gold 5
import sys
from collections import deque
input = sys.stdin.readline

"""
6 4
1 -1 0 0 0 0
0 -1 0 0 0 0
0 0 0 0 -1 0
0 0 0 0 -1 1

6
"""
n, m = map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(m)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
que = []

for i in range(m):
    for j in range(n):
        if n_list[i][j] == 1:
            que.append((i,j))

while que:
    x,y = que.pop(0)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0<=nx<m and 0<=ny<n):
            continue

        if n_list[nx][ny] == 0:
            n_list[nx][ny] = n_list[x][y] + 1
            que.append((nx,ny))
max_value = 0
flag = True
for i in range(m):
    for j in range(n):
        max_value = max(max_value, max(n_list[i]))
        if n_list[i][j] == 0:
            flag = False
            break
if flag:
    print(max_value-1)
else:
    print(-1)
