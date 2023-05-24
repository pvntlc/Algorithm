# 4179번 : 불! - Gold 4
import sys
input = sys.stdin.readline
INF = sys.maxsize
"""

"""
n, m = map(int, input().split())
visited_j = [[0] * m for _ in range(n)]
visited_f = [[INF] * m for _ in range(n)]

graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))
print(graph)

que = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == "J":
            sy, sx = i, j

        elif graph[i][j] == "F":
            que.append((i,j,0))

dx = [0,0,1,-1]
dy = [1,-1,0,0]




while que:
    y,x,count = que.pop(0)

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if not (0<=ny<m and 0<=nx<n):
            continue

        if graph[ny][nx] != "#" and visited_f[ny][nx] == 0 and graph[ny][nx] != "F":
            que.append((ny,nx,count+1))
            visited_f[ny][nx] = count +1

que = [(sy,sx,0)]
while que:
    y,x,count = que.pop(0)

    if (y == 0 or x == 0 or y == m-1 or x == n-1) and visited_j[y][x] < visited_f[y][x]:
        print(visited_j[y][x]+1)
        break


    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if not (0<=ny<m and 0<=nx<n):
            continue

        if graph[ny][nx] != "#" and visited_j[ny][nx] == 0 and not (ny == sy and nx == sx):
            que.append((ny,nx,count+1))
            visited_j[ny][nx] = count +1
else:
    print("impossible")
