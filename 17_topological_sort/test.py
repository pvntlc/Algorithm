# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

input = sys.stdin.readline
'''
6
0 1 1 0 0 0
0 1 1 0 1 1
0 0 0 0 1 1
0 0 0 0 1 1
1 1 0 0 1 0
1 1 1 0 0 0
'''


def BFS(i, j):
    que = [(i, j)]
    count = 1
    visited[i][j] = False

    while que:
        x, y = que.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not(0 <= nx < n and 0 <= ny < n):
                continue

            if visited[nx][ny] and n_list[nx][ny] == 1:
                que.append((nx, ny))
                visited[nx][ny] = False
                count += 1

    return count


n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]
answer = []
visited = [[True] * (n) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(n):
        if n_list[i][j] == 1 and visited[i][j]:
            answer.append(BFS(i, j))

if answer:
    answer.sort()
    print(len(answer))
    print(*answer)
else:
    print(0)
