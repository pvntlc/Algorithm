# 7576번 : 토마토 – Gold 5
import sys
from collections import deque
input = sys.stdin.readline

"""

"""
m, n = map(int, input().split())
n_list = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(n):
    n_list.append(list(map(int, input().split())))

que = deque()
for i in range(n):
    for j in range(m):
        if n_list[i][j] == 1:
            que.append((i,j))

while que:
    x,y = que.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<= nx < n and 0<= ny < m and n_list[nx][ny] == 0:
            n_list[nx][ny] = n_list[x][y] + 1
            que.append((nx,ny))

flag = 0
max_value = -1
for i in range(n):
    for j in range(m):
        if n_list[i][j] == 0:
            flag = 1
    max_value = max(max_value, max(n_list[i]))

if flag == 0:
    print(max_value-1)
else:
    print(-1)