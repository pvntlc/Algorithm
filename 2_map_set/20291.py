# 20291번 : 파일 정리 – Silver 3
import sys
import itertools
from collections import Counter
input = sys.stdin.readline
INF = (10)**5+1
"""

"""
def solution():
    n = int(input())
    s_list = dict()
    for _ in range(n):
        a,b = input().rstrip().split(".")
        s_list[b] = s_list.get(b,0) + 1

    for s in sorted(s_list):
        print(s, s_list[s])
solution()