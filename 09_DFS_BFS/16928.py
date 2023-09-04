# 16928번 : 뱀과 사다리 게임 - Gold 5
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
"""
3 7
32 62
42 68
12 98
95 13
97 25
93 37
79 27
75 19
49 47
67 17
"""
n, m = map(int, input().split())

ladder = dict()
snake = dict()
visited = [0] * 101

for _ in range(n):
    a,b = map(int, input().split())
    ladder[a] = b

for _ in range(m):
    a,b = map(int, input().split())
    snake[a] = b

def play():
    que = deque()
    que.append(1)

    while que:
        x = que.popleft()

        if x == 100:
            return visited[x]

        for i in range(1,7):
            nx = x + i

            if nx > 100:
                continue

            if nx in ladder.keys():
                nx = ladder[nx]

            if nx in snake.keys():
                nx = snake[nx]

            if not visited[nx]:
                visited[nx] = visited[x] + 1
                que.append(nx)
print(play())