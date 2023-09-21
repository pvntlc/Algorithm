import copy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

point = []
answer = 100

for i in range(n):
    for j in range(m):
        if board[i][j] > 0 and board[i][j] < 6:
            point.append((board[i][j],i,j))

def fill(temp_board, mm, x,y):
    for i in mm:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]

            if not (0<=nx<n and 0<=ny<m):
                break

            elif temp_board[nx][ny] == 6:
                break

            elif temp_board[nx][ny] == 0:
                temp_board[nx][ny] = -1

def dfs(temp_board, index):
    global answer
    if index == len(point):
        count = 0
        for i in range(n):
            count += temp_board[i].count(0)
        answer = min(answer, count)
        return

    temp_arr = copy.deepcopy(temp_board)
    cctv,x,y = point[index]
    for i in mode[cctv]:
        fill(temp_arr, i, x, y)
        dfs(temp_arr, index+1)
        temp_arr = copy.deepcopy(temp_board)

dfs(board, 0)
print(answer)
