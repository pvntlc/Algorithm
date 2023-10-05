# 3197번 : 백조의 호수 - Platinum 5
import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize
"""

"""
def find(x1, y1):
    if parent[x1][y1][0] < 0:
        return [x1, y1]
    parent[x1][y1] = find(parent[x1][y1][0], parent[x1][y1][1])
    return parent[x1][y1]

def union(x1,y1, x2, y2):
    px1, py1 = find(x1, y1)
    px2, py2 = find(x2, y2)

    if px1 == px2 and py1 == py2:
        return

    if parent[px1][py1][0] < parent[px2][py2][0]:
        parent[px1][py1][0] += parent[px2][py2][0]
        parent[px1][py1][1] += parent[px2][py2][1]
        parent[px2][py2] = [px1, py1]

    else:
        parent[px2][py2][0] += parent[px1][py1][0]
        parent[px2][py2][1] += parent[px1][py1][1]
        parent[px1][py1] = [px2, py2]

    return


r,c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]
que = deque()
que1= deque()
parent = [[[-1,-1] for _ in range(c)] for _ in range(r)]
time = [[0 for _ in range(c)] for _ in range(r)]
swans = []

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(r):
    for j in range(c):
        if board[i][j] == "L":
            swans.append((i, j))
            board[i][j] = "."
            if len(swans) == 2:
                break

for i in range(r):
    for j in range(c):
        if board[i][j] == '.' and time[i][j] == 0:
                time[i][j] = 1
                que.append((i,j))
                while que:
                    x, y = que.popleft()
                    union(i,j,x,y)
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if not (0 <= nx < r and 0 <= ny < c):
                            continue

                        if board[nx][ny] == 'X' and time[nx][ny] == 0:
                            time[nx][ny] = 1
                            que1.append((nx, ny))

                        if board[nx][ny] == '.' and time[nx][ny] == 0:
                            time[nx][ny] = 1
                            que.append((nx, ny))


day = 0

while find(swans[0][0], swans[0][1]) != find(swans[1][0], swans[1][1]):
    tmp = deque()
    while que1:
        x,y  = que1.popleft()
        board[x][y] = "."
        merge_point = []
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            if not (0 <= nx < r and 0 <= ny < c):
                continue

            if time[nx][ny] == 0 and board[nx][ny] == "X":
                time[nx][ny] = 1
                tmp.append((nx, ny))
            elif board[nx][ny] == ".":
                union(nx,ny,x,y)

    que1 = tmp
    day += 1
print(day)
