# 13460 : 구슬 탈출 2 - Gold 1
from collections import deque
import sys

input = sys.stdin.readline

'''

'''

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def move(d, x, y):  # d -> 위, 아래, 오른쪽, 왼쪽

    nx = x + dx[d]
    ny = y + dy[d]

    if board[ny][nx] == '#':
        return (False, x, y)

    while board[ny][nx] == '.':
        x = nx
        y = ny
        nx = x + dx[d]
        ny = y + dy[d]

    if board[ny][nx] == "O":
        return (2, nx, ny)

    else:
        if flag == 1:
            return (1, x, y)
        elif flag == 2 and RED == (x, y):
            return (1, x - dx[d], y - dy[d])
        elif flag == 3 and BLUE == (x, y):
            return (1, x - dx[d], y - dy[d])
        return (1, x, y)


for i in range(m):
    for j in range(n):
        if board[j][i] == 'R':
            RED = (i, j)
            board[j][i] = '.'

        elif board[j][i] == 'B':
            BLUE = (i, j)
            board[j][i] = '.'

que = deque()

que.append(RED)
que.append(BLUE)

flag = 1  # 1일때는 평상시, 2일때는 red가 먼저 수행된 경우, 3일때는 blue가 먼저 수행된 경우

for k in range(1, 11):

    temp = deque()
    while que:
        cred = que.popleft()
        cblue = que.popleft()

        for i in range(4):  # d -> 위, 아래, 오른쪽, 왼쪽
            if i == 0:
                if cred[1] < cblue[1]:
                    cred_st, cred_x, cred_y = move(i, cred[0], cred[1])
                    RED = (cred_x, cred_y)
                    flag = 2
                    cblue_st, cblue_x, cblue_y = move(i, cblue[0], cblue[1])
                    BLUE = (cblue_x, cblue_y)
                    flag = 1

                else:
                    cblue_st, cblue_x, cblue_y = move(i, cblue[0], cblue[1])
                    BLUE = (cblue_x, cblue_y)
                    flag = 3
                    cred_st, cred_x, cred_y = move(i, cred[0], cred[1])
                    RED = (cred_x, cred_y)
                    flag = 1

                if (cred_x, cred_y) == cred and cblue == (cblue_x, cblue_y):
                    continue

                if cred_st == 2 and (cblue_st == 1 or cblue_st == False):
                    print(k)
                    exit(0)


                elif cblue_st == 2:
                    continue

                elif cred_st == False and cblue_st == False:
                    continue

                else:
                    temp.append((cred_x, cred_y))
                    temp.append((cblue_x, cblue_y))

            elif i == 1:
                if cred[1] > cblue[1]:
                    cred_st, cred_x, cred_y = move(i, cred[0], cred[1])
                    RED = (cred_x, cred_y)
                    flag = 2
                    cblue_st, cblue_x, cblue_y = move(i, cblue[0], cblue[1])
                    BLUE = (cblue_x, cblue_y)
                    flag = 1

                else:
                    cblue_st, cblue_x, cblue_y = move(i, cblue[0], cblue[1])
                    BLUE = (cblue_x, cblue_y)
                    flag = 3
                    cred_st, cred_x, cred_y = move(i, cred[0], cred[1])
                    RED = (cred_x, cred_y)
                    flag = 1

                if (cred_x, cred_y) == cred and cblue == (cblue_x, cblue_y):
                    continue

                if cred_st == 2 and (cblue_st == 1 or cblue_st == False):
                    print(k)
                    exit(0)

                elif cblue_st == 2:
                    continue


                elif cred_st == False and cblue_st == False:

                    continue


                else:

                    temp.append((cred_x, cred_y))

                    temp.append((cblue_x, cblue_y))


            elif i == 2:
                if cred[0] > cblue[0]:
                    cred_st, cred_x, cred_y = move(i, cred[0], cred[1])
                    RED = (cred_x, cred_y)
                    flag = 2
                    cblue_st, cblue_x, cblue_y = move(i, cblue[0], cblue[1])
                    BLUE = (cblue_x, cblue_y)
                    flag = 1

                else:
                    cblue_st, cblue_x, cblue_y = move(i, cblue[0], cblue[1])
                    BLUE = (cblue_x, cblue_y)
                    flag = 3
                    cred_st, cred_x, cred_y = move(i, cred[0], cred[1])
                    RED = (cred_x, cred_y)
                    flag = 1

                if (cred_x, cred_y) == cred and cblue == (cblue_x, cblue_y):
                    continue
                if cred_st == 2 and (cblue_st == 1 or cblue_st == False):
                    print(k)
                    exit(0)
                elif cblue_st == 2:
                    continue


                elif cred_st == False and cblue_st == False:

                    continue


                else:

                    temp.append((cred_x, cred_y))

                    temp.append((cblue_x, cblue_y))


            else:
                if cred[0] < cblue[0]:
                    cred_st, cred_x, cred_y = move(i, cred[0], cred[1])
                    RED = (cred_x, cred_y)
                    flag = 2
                    cblue_st, cblue_x, cblue_y = move(i, cblue[0], cblue[1])
                    BLUE = (cblue_x, cblue_y)
                    flag = 1

                else:
                    cblue_st, cblue_x, cblue_y = move(i, cblue[0], cblue[1])
                    BLUE = (cblue_x, cblue_y)
                    flag = 3
                    cred_st, cred_x, cred_y = move(i, cred[0], cred[1])
                    RED = (cred_x, cred_y)
                    flag = 1

                if (cred_x, cred_y) == cred and cblue == (cblue_x, cblue_y):
                    continue

                if cred_st == 2 and (cblue_st == 1 or cblue_st == False):
                    print(k)
                    exit(0)
                elif cblue_st == 2:
                    continue


                elif cred_st == False and cblue_st == False:

                    continue


                else:

                    temp.append((cred_x, cred_y))
                    temp.append((cblue_x, cblue_y))

    que = temp

else:
    print(-1)
