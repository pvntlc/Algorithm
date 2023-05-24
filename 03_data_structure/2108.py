# 2108번 : 통계학 - Silver 3
import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
"""

"""
def solution():
    n = int(input())
    count = [0] * 8001
    sum = 0
    for _ in range(n):
        a = int(input())
        count[a+4000] += 1

    max_count = max(count)
    mode = mcnt = 0
    idx = 0
    med = None
    mi, ma = 4001,-4001
    for i in range(8001):
        cnt = count[i]
        if cnt == 0:
            continue
        num = i - 4000
        sum += num * count[i]
        if cnt == max_count and mcnt < 2:
            mode = num
            mcnt += 1
        mi = min(mi, num)
        ma = max(ma, num)
        idx += count[i]
        if idx >= n//2+1 and med == None:
            med = num
    print(round(sum/n), med, mode, ma-mi, sep='\n')

solution()