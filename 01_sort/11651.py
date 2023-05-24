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
        n_list.append(list(map(int, input().split())))

    n_list.sort(key = lambda x:(x[1], x[0]))

    for i in range(n):
        print(*n_list[i])
solution()