# 11279번 : 최대 힙 - Silver 2
import sys
import heapq as hq
input = sys.stdin.readline
INF = sys.maxsize
'''
'''
que = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if que:
            print(-hq.heappop(que))
        else:
            print(0)
    else:
        hq.heappush(que, -x)