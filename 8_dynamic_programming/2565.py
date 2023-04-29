# 2565번 : 전깃줄 - Gold 5
import sys
input = sys.stdin.readline
INF = sys.maxsize
'''

'''

n = int(input())
case = []
dp = [1 for _ in range(n)]

for _ in range(n):
    case.append(list(map(int, input().split())))
case.sort()

for i in range(n):
    for j in range(i):
        if case[i][1] > case[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))