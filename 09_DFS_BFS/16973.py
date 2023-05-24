# 16973번 : 직사각형 탈출 - Gold 4
import sys
from collections import deque
input = sys.stdin.readline

"""

"""

n, m = map(int, input().split())
road = []
for _ in range(n):
    road.append(list(map(int, input().split())))
h, w, sr, sc, fr, fc = map(int, input().split()) # 직사각형 크기 세로, 가로, 시작좌표, 도착좌표(좌표 -1 해줘야함)

dx = [0,0,1,-1]
dy = [1,-1, 0, 0]
visited = [[False] * m for _ in range(n)]

def check(i,j):
    for x,y in wall:
        if i<=x<i+h and j<=y<j+w:
            return False
    return True

wall = []
for i in range(n):
    for j in range(m):
        if road[i][j] == 1:
            wall.append((i,j))

que = [(sr-1, sc-1,0)]
while que:
    y, x, cnt = que.pop(0)
    visited[y][x] = True

    if y == fr-1 and x == fc-1:
        print(cnt)
        break

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0<= nx < m and 0<= ny + h -1 < n and 0<= nx + w - 1 < m:
            if not visited[ny][nx]:
                if check(ny, nx):
                    que.append((ny, nx, cnt+1))
                    visited[ny][nx] = True
else:
    print(-1)