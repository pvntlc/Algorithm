# 14503번 : 로봇 청소기 - Gold 5
import sys
input = sys.stdin.readline

'''
청소하는 영역의 개수를 구하는 프로그램
1. 현재 칸이 청소되지 않은 경우, 현재 칸 청소
2. 현재 칸의 주변 4칸 중 청소되지 않은 칸이 없는 경우에
    1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 후진한다.
    2. 바라보는 방향이 뒤쪽 칸이 벽이라서 후진할 수 없다면 작동을 멈춘다.
3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우에는
    1. 반 시계 방향으로 90도 회전한다.
    2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
    3. 1번으로 돌아간다.
'''
n, m = map(int, input().split())
r, c, d = map(int, input().split()) # 청소기 좌표
room = [list(map(int, input().split())) for _ in range(n)]
count = 0
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
direction = [[3,2,1,0], [0,3,2,1], [1,0,3,2], [2,1,0,3]]
cleaning_room = [[True] * m for _ in range(n)]

def forward(d): #0:북, 1:동, 2:남, 3:서
    global r,c
    r = r + dr[d]
    c = c + dc[d]

def backward(d):
    global r,c
    r = r - dr[d]
    c = c - dc[d]

while True:
    if room[r][c] == 0 and cleaning_room[r][c]:
        cleaning_room[r][c] = False
        count += 1

    for i in direction[d]:
        new_r = r + dr[i]
        new_c = c + dc[i]

        if room[new_r][new_c] == 0 and cleaning_room[new_r][new_c]:
            d = i
            forward(d)
            break

    else:
        backward(d)
        if room[r][c] == 1:
            break
        continue


print(count)
