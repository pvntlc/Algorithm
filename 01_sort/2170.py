import sys
from collections import deque
import heapq as hq

input = sys.stdin.readline
"""

"""

def solution():
    n = int(input())
    n_list = []
    sum = 0

    for _ in range(n):
        line = tuple(map(int, input().split()))
        n_list.append(line)

    n_list.sort()

    sum = n_list[0][1] - n_list[0][0]
    max_end = n_list[0][1]

    for x,y in n_list:
        sum += (y-x)
        if x < max_end and max_end < y:
            sum -= (max_end - x)
            max_end = y
        elif x < max_end and max_end >= y:
            sum -= (y-x)
        elif y > max_end:
            max_end = y

    print(sum)

solution()