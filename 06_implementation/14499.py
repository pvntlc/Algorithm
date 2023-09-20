# 14499번 : 주사위 굴리기 - Gold 4
import sys
input = sys.stdin.readline
INF = sys.maxsize
'''
- 이동한 칸에 쓰여 있는 수가 0이면, 주사위 바닥면의 쓰여 있는 수가 칸에 복사.
- 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사, 칸은 0이 됨.
4 2 0 0 8
0 2
3 4
5 6
7 8
4 4 4 1 3 3 3 2

0
0
3
0
0
8
6
3
'''
n, m, x, y, k = map(int, input().split())
num_list = [list(map(int, input().split())) for _ in range(n)]
oper = list(map(int, input().split()))
dice = [INF,0,0,0,0,0,0]

dx = [1,-1,0,0] #동,서,북,남
dy = [0,0,-1,1]

top = 1

def solve(number):
    global top;
    if top == 1:
        if number == 1:
            top = 4
        elif number == 2:
            top = 3
        elif number == 3:
            top = 5
        elif number == 4:
            top = 2

    elif top == 6:
        if number == 1:
            top = 3
        elif number == 2:
            top = 4
        elif number == 3:
            top = 2
        elif number == 4:
            top = 5

    elif top == 3:
        if number == 1:
            top = 1
        elif number == 2:
            top = 6
        elif number == 3:
            top = 5
        elif number == 4:
            top = 2

    elif top == 4:
        if number == 1:
            top = 6
        elif number == 2:
            top = 1
        elif number == 3:
            top = 2
        elif number == 4:
            top = 5

    elif top == 2:
        if number == 1:
            top = 4
        elif number == 2:
            top = 3
        elif number == 3:
            top = 1
        elif number == 4:
            top = 6

    elif top == 5:
        if number == 1:
            top = 3
        elif number == 2:
            top = 4
        elif number == 3:
            top = 6
        elif number == 4:
            top = 1

for num in oper:
    nx = x + dx[num-1]
    ny = y + dy[num-1]

    if not (0<=nx<m and 0<=ny<n):
        continue

    solve(num)
    x = nx
    y = ny

    if num_list[y][x] == 0:
        num_list[y][x] = dice[7-top]
        dice[7-top] = 0

    elif dice[7-top] == 0:
        dice[7-top] = num_list[y][x]
        num_list[y][x] = 0


    print("top : ", top)
    print("숫자 : ",dice[1:])
    print(dice[top])
    print()




