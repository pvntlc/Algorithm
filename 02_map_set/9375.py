# 9375번 : 패션왕 신해빈 – Silver 3
import sys
import math
import itertools
from collections import Counter
input = sys.stdin.readline
INF = (10)**5+1
"""

"""
def solution():
    for _ in range(int(input())):
        c_dict = dict()
        n = int(input())
        for _ in range(n):
            a,b = input().rstrip().split()
            if b not in c_dict:
                c_dict[b] = 1
            else:
                c_dict[b] += 1
        tot = 1
        for value in c_dict.values():
            tot *= value+1
        print(tot-1)
solution()