import sys
from collections import deque
import heapq as hq

input = sys.stdin.readline
"""

"""
def sum_d(x):
    sum = 0
    for i in x:
        if i.isdigit() == True:
            sum += int(i)
    return sum

def solution():
    n = int(input())
    n_list = [list(input().rstrip()) for _ in range(n)]
    n_list.sort(key = lambda x : (len(x), sum_d(x), x))
    for x in n_list:
        print(*x,sep="")
solution()