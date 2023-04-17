# 11727번 : 2×n 타일링 2 - Silver 3
import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize
"""
2*n 크기의 직사각형을 1x2, 2x1, 2x2 타일로 채우는 문제
길이가 n인 크기의 직사각형을 채울 때,
1. n-1과 1 크기로 나눈다면
- 1x2의 직사각형 하나만 들어가는 한 가지 경우의 수만 가능하다.
2. n-2와 2 크기로 나눈다면
- 2x1 직사각형 두개와 2x2 정사각형 타일로 채우는 방법이 있으므로 총 두 가지가 가능하다.
따라서, 점화식은 다음과 같다.
dp[i] = dp[i-1] + 2 * dp[i-2]
"""

n = int(input())
dp = [0, 1, 3] + [0] * (n-2)
for i in range(3, n+1):
    dp[i] = (dp[i-1] + 2* dp[i-2])  % 10007
print(dp[n])
