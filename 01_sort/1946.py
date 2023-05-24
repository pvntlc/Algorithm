import sys
from collections import deque
import heapq as hq

input = sys.stdin.readline
"""

"""

def solution():
    T = int(input())
    for _ in range(T):
        count = 0
        n = int(input())
        n_list = [list(map(int, input().split())) for _ in range(n)]
        n_list.sort()
        max_rank = n+1
        for i in range(n):
            if n_list[i][1] < max_rank:
                count += 1
                max_rank = n_list[i][1]
        print(count)
solution()