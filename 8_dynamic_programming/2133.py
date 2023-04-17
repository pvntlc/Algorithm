# 2133번 : 타일 채우기 - Gold 4
import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize
"""
3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수 구하기.
1. 
문자열을 n번 이하로 분할 가능할 때, 분할된 각 문자열에서 가장 많은 알파벳이 등장한 횟수의 최댓값을 최소화 시키고자 한대 그 최소화된 값을 찾는 문제거든...?
"""

n = int(input())
dp = [0, 1, 3] + [0] * (n-2)
for i in range(3, n+1):
    dp[i] = (dp[i-1] + 2* dp[i-2])  % 10007
print(dp[n])
