# 3190번 : 뱀 - Gold 4
import sys
input = sys.stdin.readline
INF = sys.maxsize
'''
https://www.acmicpc.net/problem/3190

1. N x N 정사각 보드 위에서 진행된다.
2. 뱀은 가장 상단 좌측에 위치하고, 뱀의 길이는 1이다. 처음 방향은 오른쪽이다.
3. 뱀은 몸길이를 늘려 머리를 다음 칸에 위치시킨다.
4. 만약 벽이나 자기 자신의 몸과 부딪히면 게임이 끝난다.
5. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
6. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여 꼬리가 위치한 칸을 비워준다.
7. 이럴 때, 게임이 몇 초에 끝나는지 계산하라.

첫 째 줄에 보드의 크기 N이 주어지고, 다음 줄은 사과의 개수 K가 주어진다.
다음 K개의 줄에는 사과의 위치가 주어진다.
다음 줄에는 뱀의 방향 변환 횟수 L이 주어진다.
L개의 줄에는 방향 변환 정보. X초가 끝난 뒤에 C방향으로 회전. (L이면 왼쪽, D는 오른쪽)

입력
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

출력
9
'''
d = [(0,1), (1,0), (0,-1), (-1,0)] #오른쪽, 아래쪽, 왼쪽, 위쪽 방향.

N = int(input())
n_list = [[0 for _ in range(N)] for _ in range(N)]

K = int(input())
for _ in range(K):
    x,y = map(int, input().split())
    n_list[x-1][y-1] = 1
L = int(input())
direction = []

for _ in range(L):
    direction.append(list(input().split()))


cx, cy, cd = 0, 0, 0
snake = [(cx,cy)]
time = 1

flag = True
number = 0

for i in range(L):
    for k in range(int(direction[i][0])-number):
        cx += d[cd][0]
        cy += d[cd][1]

        if (cx,cy) in snake or not (0<=cx<N and 0<=cy<N):
            flag = False
            break

        elif n_list[cx][cy] == 1:
            n_list[cx][cy] = 0
            snake.append((cx,cy))
            time += 1
        else:
            snake.pop(0)
            snake.append((cx,cy))
            time += 1

    number = int(direction[i][0])

    if direction[i][1] == 'D':
        cd += 1
        if cd == 4:
            cd = 0
    else:
        cd -= 1
        if cd == -1:
            cd = 3

    if not flag:
        break

while flag:
    cx += d[cd][0]
    cy += d[cd][1]

    if (cx, cy) in snake or not (0 <= cx < N and 0 <= cy < N):
        flag = False
        break

    elif n_list[cx][cy] == 1:
        snake.append((cx, cy))
        time += 1
    else:
        snake.pop(0)
        snake.append((cx, cy))
        time += 1

print(time)
