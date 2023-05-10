# 5397번 : 키로거 - Silver 2
import sys
from collections import deque

input = sys.stdin.readline

"""
"""

for _ in range(int(input())):
    front = deque()
    back = deque()
    line = input().rstrip()

    for i in line:
        if i == "<":
            if front:
                back.appendleft(front.pop())
        elif i == ">":
            if back:
                front.append(back.popleft())
        elif i == "-":
            if front:
                front.pop()
        else:
            front.append(i)

    print(''.join(front), ''.join(back), sep="")