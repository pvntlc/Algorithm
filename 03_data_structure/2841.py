# 2841번 : 외계인의 기타 연주 – Silver 1
import sys
from collections import deque
from collections import Counter

input = sys.stdin.readline
"""

"""


def solution():
    n, p = map(int, input().split())  # 음의 수 n과 프랫 수 p.
    n_list = [[0] for _ in range(7)]  # 미리 0을 넣어놓으면, 비어있는지 확인을 안 해도 된다.
    count = 0

    for _ in range(n):
        a, b = map(int, input().split())
        while n_list[a][-1] > b:
            count += 1
            n_list[a].pop()

        if n_list[a][-1] == b:
            continue

        n_list[a].append(b)
        count += 1

    print(count)


solution()