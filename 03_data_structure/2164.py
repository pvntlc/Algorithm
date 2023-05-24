# 2164번 : 카드2 - Silver 4
import sys
from collections import deque
input = sys.stdin.readline
"""

"""
def solution():
    n = int(input())
    que = deque()
    for i in range(n):
        que.append(i+1)

    while len(que) != 1:
        que.popleft()
        que.append(que.popleft())
    print(*que)
solution()