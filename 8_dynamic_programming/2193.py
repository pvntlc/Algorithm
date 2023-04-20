# 2193번 : 이친수 - Silver 3
import sys
from collections import deque
input = sys.stdin.readline
"""

"""
s = [0, 1, 1]
for i in range(3, 91):
  s.append(s[i - 2] + s[i - 1])
n = int(input())
print(s[n])