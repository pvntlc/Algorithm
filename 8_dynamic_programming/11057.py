# 11057번 : 오르막 수 - Silver 1
import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize
"""

"""
n = int(input())
dp = [[1]*10] + [[0]*10 for _ in range(n-1)]
for i in range(0, n):
    for j in range(10):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(sum(dp[n-1]) % 10007)