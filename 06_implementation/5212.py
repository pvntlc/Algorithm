# 5212번 : 지구 온난화 - Silver 2
import sys
import copy
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int, input().split())
n_list = [['.'] * (m+2)] + [['.'] + list(input().rstrip()) + ['.'] for _ in range(n)] + [['.'] * (m+2)]

answer = copy.deepcopy(n_list)
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for i in range(1,n+1):
    for j in range(1,m+1):
        if n_list[i][j] == 'X':
            count = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if not (0<=nx<n+2 and 0<=ny<m+2):
                    continue

                if n_list[nx][ny] == '.':
                    count += 1
            if count >= 3:
                answer[i][j] = '.'
min_x = INF
min_y = INF
max_x = 0
max_y = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if answer[i][j] == 'X':
            min_x = min(min_x, i)
            min_y = min(min_y, j)
            max_x = max(max_x, i)
            max_y = max(max_y, j)
answer_1 = answer[min_x:max_x+1]
for i in range(max_x - min_x + 1):
    for j in range(min_y, max_y+1):
        print(answer_1[i][j], end="")
    print()