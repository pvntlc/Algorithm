# 1253번 : 좋다 - Gold 4
import sys

input = sys.stdin.readline
INF = sys.maxsize

"""
https://www.acmicpc.net/problem/1253

10
1 2 3 4 5 6 7 8 9 10

8
"""

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
answer = 0
for i in range(n):
    start = 0
    end = n - 1

    while start != end:
        if start == i:
            start += 1
            continue

        if end == i:
            end -= 1
            continue
            # 음수가 가능하기 때문에 겹치는 것 방지.

        temp = n_list[start] + n_list[end]

        if n_list[i] > temp:
            start += 1
        elif n_list[i] < temp:
            end -= 1
        else:
            answer += 1
            break
print(answer)