import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize
"""
3 x 2일 때
- 타일을 채우는 경우의 수는 총 3가지.
3 x 4일 때
- 3 x 2일 때 타일을 채우는 경우의 수가 총 3가지 이므로 3 x 3 = 9가지
- 3 x 4일 때만 가능한 타일을 채우는 경우의 수가 2가지.
- 총 11가지 가능함.
그래서 점화식을 세워보면,
DP[i] = DP[i - 2] * 3 + DP[i-4] * 2 + DP[i-6] * 2 + ... 가 되는 것이다.
"""

n = int(input())
dp = [0 for _ in range(31)]
dp[2] = 3
for i in range(4,n+1) :
    if i%2 == 0 :
        dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2
    else :
        dp[i] = 0
print(dp[n])