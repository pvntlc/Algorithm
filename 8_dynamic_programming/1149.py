# 1149번 : RGB 거리 - Silver 1
import sys
input = sys.stdin.readline
INF = sys.maxsize
'''
3
  빨 초 파
1 26 40 83
2 49 60 57
3 13 89 99

dp[i][1] = min(dp[i-1][2] + color[i][1], dp[i-1][3] + color[i][1])
'''

n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1,n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + dp[i][1]
    dp[i][2] = min(dp[i - 1][1], dp[i - 1][0]) + dp[i][2]
print(min(dp[n-1]))