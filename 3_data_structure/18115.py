#18115번 : 카드 놓기 - Silver 3
import sys
from collections import deque
input = sys.stdin.readline

def solution():
    n = int(input())


    number = list(map(int, input().split()))
    number.reverse()
    que = deque()

    dq = deque()
    for i in range(n):
        if number[i] == 1:
            dq.appendleft(i + 1)
        elif number[i] == 2:
            dq.insert(1, i + 1)
        elif number[i] == 3:
            dq.append(i + 1)
    print(*dq)
solution()