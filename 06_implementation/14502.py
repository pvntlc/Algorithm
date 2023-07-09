# 14502번 : 연구소 - Gold IV
import copy
import sys
input = sys.stdin.readline

'''
1. 0은 빈칸, 1은 벽, 2는 바이러스가 있는 곳.
2, 첫째 줄에 지도의 세로 크기와 가로 크기가 주어진다.
3. 벽을 세 개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다.

pypy3로 제출해야 함 !

- 입력
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

- 출력
27
'''
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    que = []

    test_map = copy.deepcopy(n_list)

    for i in range(n):
        for j in range(m):
            if n_list[i][j] == 2:
                que.append((i,j))

    while que:
        x,y = que.pop(0)

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0<=new_x<n and 0<=new_y<m:
                if test_map[new_x][new_y] == 0:
                    test_map[new_x][new_y] = 2
                    que.append((new_x, new_y))

    global result
    count = 0
    for i in range(n):
        for j in range(m):
            if test_map[i][j] == 0:
                count += 1
    result = max(result, count)

def make_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for k in range(m):
            if n_list[i][k] == 0:
                n_list[i][k] = 1
                make_wall(count + 1)
                n_list[i][k] = 0

n, m = map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(n)]
result = 0
make_wall(0)
print(result)



