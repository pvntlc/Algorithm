# 20207번 : 달력 - Gold 5
import sys
from collections import deque
input = sys.stdin.readline

"""
"""

n = int(input())
n_list = [0] * 366
for _ in range(n):
    s,e = map(int, input().split())
    for i in range(s, e+1):
        n_list[i] += 1
count = 0
answer = 0
max_value = 0
for i in n_list:
    if i == 0:
        answer += count * max_value
        count = 0
        max_value = 0
    else:
        count += 1
        max_value = max(max_value, i)
answer += count * max_value
print(answer)