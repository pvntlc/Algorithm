# 21608번 : 상어 초등학교 - Gold 5
import sys
input = sys.stdin.readline
INF = sys.maxsize - 1
"""
빈 자릿수도 세야하고, 주위 선호도 세야하네
"""

n = int(input())
seat = [[0] * (n) for _ in range(n)]
n_list = []
for _ in range(n**2):
    n_list.append(list(map(int, input().split())))
def find_seat(list):
    score = []
    for i in range(n):
        line = []
        for j in range(n):
            if seat[i][j] != 0:
                line.append([-INF, -INF, i,j])
            else:
                line.append([0,0,i,j])
        score.append(line)

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(n):
        for j in range(n):
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]

                if not (0<=x<n and 0<=y<n):
                    continue

                if seat[x][y] == 0:
                    score[i][j][1] += 1

                if seat[x][y] in list[1:]:
                    score[i][j][0] += 1
    for i in range(n):
        score[i].sort(key = lambda x:(-x[0], -x[1], x[2], x[3]))
    score.sort(key = lambda x:(-x[0][0], -x[0][1], x[0][2], x[0][3]))
    return score[0][0][2], score[0][0][3]

answer = []
for i in range(n**2):
    s = n_list[i][0]
    x,y = find_seat(n_list[i])
    seat[x][y] = s
    answer.append((x,y))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
sum = 0
for i in range(n**2):
    x,y = answer[i][0], answer[i][1]
    count = 0
    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]

        if not (0 <= xx < n and 0 <= yy < n):
            continue

        if seat[xx][yy] in n_list[i][1:]:
            count +=1

    if count == 0:
        continue
    elif count ==1:
        sum += 1
    elif count == 2:
        sum += 10
    elif count == 3:
        sum += 100
    elif count == 4:
        sum += 1000
print(sum)







