# 1017번 : 제곱 ㄴㄴ수 - Gold 1
import sys
from collections import defaultdict
input = sys.stdin.readline
INF = sys.maxsize
'''
https://www.acmicpc.net/problem/1017

1000000000000 1000000100000
'''

n, m = map(int, input().split())
check = [0 for _ in range(m-n+1)]
answer = m-n+1
i = 2
while i*i <= m:
    num = i * i

    if n % num == 0:
        cur_num = n
    else:
        cur_num = ((n // num)+1) * num

    for j in range(cur_num, m+1, num):
        if check[j-n] == 0:
            check[j-n] = 1
            answer -= 1
    i += 1
print(answer)