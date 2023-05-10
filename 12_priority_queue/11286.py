# 11286번 : 절댓값 힙 – Silver 1
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
            print(hq.heappop(que)[1])
        else:
            print(0)
    else:
        hq.heappush(que, (abs(x), x))