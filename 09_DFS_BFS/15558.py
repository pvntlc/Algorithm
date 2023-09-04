# 1555번 : 점프 게임 - Gold 5
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
"""
7 3
1110110
1011001

1
"""

def dfs():
    n, k = map(int, input().split())
    graph = [list(map(int, input().rstrip())) for _ in range(2)]
    visit = [[0] * n for _ in range(2)]
    que = [(0,0,0)]

    while que:
        x,y,time = que.pop()
        for nx,ny in (x,y+1), (x,y-1), (x^1,y+k):
            if ny >= n:
                return 1
            if ny <= time or graph[nx][ny] == 0 or visit[nx][ny] == 1:
                continue
            que.append((nx,ny, time+1))
            visit[nx][ny] = 1
    return 0
print(dfs())