# 18405번 : 경쟁적 전염 - Gold 5
import sys
from collections import deque
input = sys.stdin.readline

"""

"""

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
time = [[0] * n for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def play(s,rx,ry):
    que = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                continue
            que.append((graph[i][j],i,j))
    que.sort()

    while que:
        temp, x,y = que.pop(0)


        if x == rx-1 and y == ry-1:
            if time[x][y] <= s:
                return graph[x][y]
            else:
                return 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nx<n and 0<=ny<n):
                continue

            if graph[nx][ny] == 0:
                que.append((1,nx,ny))
                graph[nx][ny] = graph[x][y]
                time[nx][ny] = time[x][y] + 1

print(play(s,x,y))
