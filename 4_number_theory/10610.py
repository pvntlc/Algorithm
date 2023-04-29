# 10610번 : 30 - Silver 4
import sys
import itertools
input = sys.stdin.readline
"""

"""


def solution():
    n = list(map(int,input().rstrip()))
    n.sort(reverse=True)
    if sum(n) % 3 == 0 and n[-1] == 0:
        print(*n,sep="")
        return
    else:
        print(-1)
        return
solution()