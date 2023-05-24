# 19583번 : 싸이버개강총회 – Silver 1
import sys
import itertools
from collections import Counter
input = sys.stdin.readline
INF = (10)**5+1
"""

"""
def solution():
    s,e,q = input().split()
    answer1 = set()
    answer2 = set()
    while (True):
        try:
            time, name = input().split()
            if time <= s:
                answer1.add(name)
            elif e<= time <= q:
                answer2.add(name)
        except:
            print(len(answer1.intersection(answer2)))
            break
solution()