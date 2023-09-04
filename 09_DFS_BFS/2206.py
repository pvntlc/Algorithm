# 2206번 : 벽 부수고 이동하기 - Gold 3
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
"""
6 4
0100
1110
1000
0000
0111
0000

15
"""

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1
dx = [1,-1,0,0]
dy = [0,0,1,-1]


def dfs():
    que = deque()
    que.append((0, 0, 0))
    while que:
        x,y,c = que.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][c]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nx<n and 0<=ny<m):
                continue

            if graph[nx][ny] == 1 and c == 0:
                que.append((nx,ny,1))
                visited[nx][ny][1] = visited[x][y][0] + 1

            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                que.append((nx,ny,c))
                visited[nx][ny][c] = visited[x][y][c] + 1
    return -1
print(dfs())
print(visited)
