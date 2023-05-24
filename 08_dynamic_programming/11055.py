# 11055번 : 가장 큰 증가하는 부분 수열 - Silver 2
import sys
input = sys.stdin.readline
'''
input()
dp = [0] * 1001
for i in map(int, input().split()):
    dp[i] = max(dp[:i]) + i

print(max(dp))
'''

n = int(input())
n_list = list(map(int, input().split()))
dp = [n_list[0]] + [0] * (n-1)

for i in range(1, n):
    for j in range(i):
        if n_list[i] > n_list[j]:
            dp[i] = max(dp[i], dp[j] + n_list[i])
        else:
            dp[i] = max(dp[i], n_list[i])

print(max(dp))

