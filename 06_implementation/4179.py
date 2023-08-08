import sys
import heapq

input = sys.stdin.readline

'''
보석이 총 n개, 가방은 k개.
각 보석마다 무게 m, 가격 v.
가방에 담을 수 있는 최대 무게 c.
'''

r,c = map(int, input().split()) # 행과 열 board[r][c]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

graph = []

que_j = []
que_f = []
visited_j = [[0] * c for _ in range(r)]
visited_f = [[0] * c for _ in range(r)]

for i in range(r):
    temp = list(input())

    for j in range(len(temp)):
        if temp[j] == "J":
            que_j.append((i, j))
            visited_j[i][j] = 1

        elif temp[j] == "F":
            que_f.append((i, j))
            visited_f[i][j] = 1

    graph.append(temp)

def bfs():
    while que_f:
        x,y = que_f.pop(0)

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if not visited_f[nx][ny] and graph[nx][ny] != "#":
                    visited_f[nx][ny] = visited_f[x][y] + 1
                    que_f.append((nx, ny))

    while que_j:
        x, y = que_j.pop(0)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if not visited_j[nx][ny] and graph[nx][ny] != "#":
                    if not visited_f[nx][ny] or visited_f[nx][ny] > visited_j[x][y] + 1:
                        visited_j[nx][ny] = visited_j[x][y] + 1
                        que_j.append((nx, ny))
            else:
                return visited_j[x][y]

    return "IMPOSSIBLE"

print(bfs())