# 94655번 : 스티커 - Silver 1
import sys
input = sys.stdin.readline
'''

'''
for _ in range(int(input())):
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue
    else:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]

        for i in range(2, n):
            dp[1][i] += max(dp[0][i-2], dp[0][i-1])
            dp[0][i] += max(dp[1][i - 2], dp[1][i - 1])
    print(max(dp[1][n-1], dp[0][n-1]))
