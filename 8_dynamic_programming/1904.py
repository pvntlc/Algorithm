# 1904번 : 01타일 - Silver 3
import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize
"""
1 - 1 (1)
2 - 11 00 (2)
3 - 111 100 001 (3)
4 - 0011 0000 1001 1100 1111 (5)
5 - 10011 00111 10000 00100 00001 11001 11100 11111 (8)
"""
n = int(input())
dp = [0,1,2] + [0] * (n-2)


for k in range(3,n+1):
    dp[k] = (dp[k-1]+ dp[k-2])%15746
print(dp[n])