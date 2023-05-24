# 11726번 : 2 x n 타일링 - Silver 3
import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize
"""
2*n 크기의 직사각형을 1x2, 2x1의 타일로 채우는 문제.
n이 1일 때는 1개, 2일 때는 2개, 3일 때는 3개, 4일 때는 5개, 5일 때는 8개이므로,
dp[i] = dp[i-1] + dp[i-2]의 점화식 형태로 나타낼 수 있다.
"""

n = int(input())
dp = [0, 1, 2] + [0] * (n-2)
for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2])  % 10007
print(dp[n])
