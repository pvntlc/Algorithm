# 1932번 : 정수 삼각형 – Silver 1
import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize
"""

"""
n_list = []
n = int(input())
for _ in range(n):
    n_list.append(list(map(int, input().split())))
dp = [[0] * i for i in range(1,n+1)]
dp[0][0] = n_list[0][0]

for i in range(n-1):
    for j in range(len(n_list[i])):
        if dp[i+1][j] < dp[i][j] + n_list[i+1][j]:
            dp[i+1][j] = dp[i][j] + n_list[i+1][j]

        if dp[i+1][j+1] < dp[i][j] + n_list[i+1][j+1]:
            dp[i+1][j+1] = dp[i][j] + n_list[i+1][j+1]
print(max(dp[n-1]))