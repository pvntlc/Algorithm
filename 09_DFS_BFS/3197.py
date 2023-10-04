# 3197번 : 백조의 호수 - Platinum 5
import sys
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
que = []
que1= []
parent = [[[-1,-1] for _ in range(c)] for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)]
visited1 = [[0 for _ in range(c)] for _ in range(r)]
swans = []

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(r):
    for j in range(c):
        if (board[i][j] == '.' or board[i][j] == 'L'):
            que1.append((i,j))
            if not visited[i][j]:
                if board[i][j] == 'L':
                    swans.append((nx,ny))
                visited[i][j] = True
                que.append((i,j))
                while que:
                    x, y = que.pop(0)
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if not (0 <= nx < r and 0 <= ny < c):
                            continue

                        if (board[nx][ny] == '.' or board[nx][ny] == 'L') and not visited[nx][ny]:
                            if board[nx][ny] == 'L':
                                swans.append((nx, ny))
                            visited[nx][ny] = True
                            que.append((nx, ny))
                            union(i,j,nx,ny)

while que1:
    x,y = que1.pop(0)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0<=nx<r and 0<=ny<c):
            continue

        if board[nx][ny] == 'X':
            que1.append((nx,ny))
            board[nx][ny] = '.'