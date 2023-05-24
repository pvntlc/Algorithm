# 11333번 : 4 x n 타일링 - Gold 2
import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize
"""
4*n 크기의 직사각형을 1x3, 3x1 타일로 채우는 문제

"""

n = int(input())
dp = [0, 1, 3] + [0] * (n-2)
for i in range(3, n+1):
    dp[i] = (dp[i-1] + 2* dp[i-2])  % 10007
print(dp[n])
