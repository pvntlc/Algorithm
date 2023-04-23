# 2156 : 포도주 시식 - Silver 1
import sys
input = sys.stdin.readline
"""

"""

n = int(input())
list = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1)
dp[1] = list[1]
if n > 1:
    dp[2] = list[1] + list[2]

for i in range(3,n+1):
    dp[i] = max(dp[i-3] + list[i-1] + list[i], dp[i-2] + list[i], dp[i-1])
print(max(dp))