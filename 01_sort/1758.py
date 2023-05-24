import sys
from collections import deque
import heapq as hq

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

"""

"""
def solution():
    n = int(input())
    n_list =[]

    for _ in range(n):
        n_list.append(int(input()))
    n_list.sort(reverse=True)

    sum = 0
    for i in range(n):
        if (n_list[i] - i) > 0:
            sum += (n_list[i] - i)
        else:
            break
    print(sum)
solution()