# 11000번 : 강의실 배정 - Gold 5
import sys
import heapq as hq
input = sys.stdin.readline
INF = sys.maxsize
'''

'''
n = int(input())
time = [tuple(map(int, input().split())) for _ in range(n)]
time.sort()
que = [-1]

for start, end in time:
    if que[0] <= start:
        hq.heappop(que)
    hq.heappush(que,end)

print(len(que))