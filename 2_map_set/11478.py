# 11478번 : 서로 다른 부분 문자열의 개수 - Silver 3
import sys
import itertools
from collections import Counter
input = sys.stdin.readline
INF = (10)**5+1
"""

"""
def solution():
    n_list = input().rstrip()
    l_set = set()
    for i in range(0, len(n_list)):
        for j in range(i, len(n_list)):
            l_set.add(n_list[i:j+1])
    print(len(l_set))
solution()