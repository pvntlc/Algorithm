# 11659번 : 구간 합 구하기 - Silver 3
import sys
input = sys.stdin.readline
INF = sys.maxsize

"""
"""

n, m = map(int, input().split())
n_list = list(map(int, input().split()))
sum_list = [0]

for i in range(n):
    sum_list.append(sum_list[-1] + n_list[i])

for i in range(m):
    s, e = map(int, input().split())
    print(sum_list[e] - sum_list[s-1])