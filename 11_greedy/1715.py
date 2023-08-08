# 1715번 : 카드 정렬하기 - Gold 4
import sys
import heapq as hq
input = sys.stdin.readline

'''

'''
n = int(input())
que = []
for _ in range(n):
    hq.heappush(que, int(input()))

answer = 0
for _ in range(n-1):
    a = hq.heappop(que)
    b = hq.heappop(que)
    answer += a + b
    hq.heappush(que, a+b)

print(answer)