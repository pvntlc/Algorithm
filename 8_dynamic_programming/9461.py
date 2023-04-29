# 9461번 : 파도반 수열 - Silver 3
import sys
input = sys.stdin.readline

t = int(input())
dp = [0,1,1,1] + [0] * (97)

for i in range(3, 101):
    dp[i] = dp[i-3] + dp[i-2]


for i in range(t):
    n = int(input())
    print(dp[n])