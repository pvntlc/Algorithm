# 2776번 : 암기왕 - Silver 4
import sys
input = sys.stdin.readline
INF = (10)**5+1
"""

"""
def solution():
    for _ in range(int(input())):
        n = int(input())
        n_list = set(map(int, input().split()))
        m = int(input())
        print('\n'.join('1' if i in n_list else '0' for i in map(int, input().split())))
solution()