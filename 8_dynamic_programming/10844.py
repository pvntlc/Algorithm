# 10844번 : 쉬운 계단 수 - Silver 1
import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize
"""

"""
n = int(input())
dp = [[1]*10 for _ in range(n)]
dp[0][0] = 0

for i in range(1, n):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[n-1]) % 1000000000)