# 4949번 : 균형잡힌 세상 - Silver 4
import sys
import math
import itertools
from collections import deque
input = sys.stdin.readline
INF = (10)**5+1
"""

"""
def solution():
    while True:
            cnt = 0
            que = deque()
            n_list = list(input().rstrip())
            for i in n_list:
                if i == "(" or i == "[":
                    que.append(i)
                elif i == ")":
                    if len(que) == 0:
                        print("no")
                        break
                    if que.pop() == "(":
                        continue
                    else:
                        print("no")
                        break
                elif i == "]":
                    if len(que) == 0:
                        print("no")
                        break
                    if que.pop() == "[":
                        continue
                    else:
                        print("no")
                        break
                elif i == ".":
                    if cnt == 0:
                        return
                    if len(que) == 0:
                        print("yes")
                    else:
                        print("no")
                    break
                cnt += 1

solution()