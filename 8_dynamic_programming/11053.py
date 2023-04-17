# 11053번 : 가장 긴 증가하는 부분 수열 – Silver 2
import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize
"""

"""

n = int(input())
n_list = list(map(int, input().split()))
dp = [0] * n
for i in range(n):
    for j in range(i):
        if n_list[i] > n_list[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))