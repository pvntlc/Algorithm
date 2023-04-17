import sys
from collections import deque
import heapq as hq

input = sys.stdin.readline
"""

"""

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort(reverse=True)
    sum = 0

    for i in range(n):
        sum += a[i] * b[i]

    print(sum)
solution()