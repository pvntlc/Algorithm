# 1918번 : 후위 표기식 - Gold 2
import sys
from collections import deque
input = sys.stdin.readline
"""
1. 피연산자는 바로 출력한다.
2. 연산자가 들어올 경우 자기보다 우선순위가 높거나 같은 연산자는 모두 출력한다.
3. (가 들어오면 무조건 담고, )가 들어오면 (가 나갈 때까지 모두 출력한다.
"""
def solution():
    priority = dict()
    priority["+"] = 1
    priority["-"] = 1
    priority["*"] = 2
    priority["/"] = 2

    que = []

    n = input().rstrip()
    for alpha in n:

        if 65 <= ord(alpha) <= 90:
            print(alpha,end="")

        elif alpha == '(':
            que.append(alpha)

        elif alpha in priority:
            while que and que[-1] != '(' and priority[alpha] <= priority[que[-1]]:
                print(que.pop(),end="")
            que.append(alpha)

        elif alpha == ')':
            while True:
                if que[-1] == '(':
                    que.pop()
                    break
                else:
                    print(que.pop(),end="")
    while que:
        print(que.pop(),end="")

solution()