# 21921번 : 블로그 - Silver 3
import sys
input = sys.stdin.readline
INF = sys.maxsize

"""
5 2
1 4 2 5 1
"""

n, x = map(int, input().split())
n_list = list(map(int, input().split()))
start, end = 0, x-1
temp = sum(n_list[start:end+1])
max_value = temp
count = 1

while end != n-1:
    temp = temp - n_list[start] + n_list[end+1]
    if max_value == temp:
        count += 1
    elif temp > max_value:
        max_value = temp
        count = 1
    start += 1
    end += 1

if max_value == 0:
    print("SAD")
else:
    print(max_value, count, sep="\n")