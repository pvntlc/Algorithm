# 5547번 : 일루미네이션 - Gold 4
import sys
from collections import deque
input = sys.stdin.readline

"""
00 01 02 03 04 05 06 07
10 11 12 13 14 15 16 17
20 21 22 23 24 25 26 27
"""

n, m = map(int, input().split())
building = [list(map(int, input().split())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]

que = []
dx = [-1, 0, 1, 0, -1, -1]
dy = [-1, -1, 0, 1, 1, 0]
answer = 0
while que:
    x, y = que.pop(0)
    count = 0
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0<=nx<n or 0<=ny<m):
            continue

        if building[ny][nx] == 1:
            count += 1

        if not visited[ny][nx]:
            que.append((nx, ny))
            visited[ny][nx] = True
    answer += (6-count)

print(answer)
