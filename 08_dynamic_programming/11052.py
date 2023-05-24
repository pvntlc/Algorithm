# 11052번 : 카드 구매하기 - Silver 1
import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize
"""

"""

n = int(input())
line = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i], line[j] + dp[i-j])
print(dp[n])