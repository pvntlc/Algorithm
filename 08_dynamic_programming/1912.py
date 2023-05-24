# 1912번 : 연속합 - Silver 2
import sys
input = sys.stdin.readline
INF = sys.maxsize
'''
10
10 -4 3 1 5 6 -35 12 21 -1

>>>
10 6 9 10 15 21 -14 12 33 32
'''

n = int(input())

n_list = list(map(int, input().split()))
dp = [n_list[0]] + [-INF+1] * (n-1)
for i in range(1, n):
    dp[i] = max(n_list[i], n_list[i] + dp[i-1])
print(max(dp))