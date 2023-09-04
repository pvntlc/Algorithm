# 2589번 : 보물섬 - Gold 5
import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize
"""
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW

8
"""
r,c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(rr,cc):
    que = deque()
    que.append((rr,cc))
    visited = [[0] * c for _ in range(r)]
    visited[rr][cc] = 1
    value = 0
    while que:
        x,y = que.popleft()
        value = max(value, visited[x][y])

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nx<r and 0<=ny<c):
                continue

            if graph[nx][ny] == 'L' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                que.append((nx,ny))
    return value-1

value = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'L':

            value = max(value, dfs(i,j))

print(value)