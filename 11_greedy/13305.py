# 13305번 : 주유소 – Silver 3
import sys
import heapq as hq
input = sys.stdin.readline
INF = sys.maxsize
'''

'''


n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))
min_price = price[0]
answer = 0
for i in range(n-1):
    if price[i] < min_price:
        min_price = price[i]
    answer += min_price * distance[i]
print(answer)