# 1935번 : 후위 표기식2 - Silver 3
import sys
import itertools
input = sys.stdin.readline
"""
ABC*+DE/-

65-90
A
"""
def solution():
    n = int(input())
    line = list(input().rstrip())
    stack = []
    oper = ["+", "-", "*", "/"]
    alphabet = dict()
    for i in range(65,65+n):
        alphabet[chr(i)] = float(input())

    for x in line:
        if x in oper:
            num1 = stack.pop()
            num2 = stack.pop()
            if x == oper[0]:
                stack.append(num1+num2)
            elif x == oper[1]:
                stack.append(num2-num1)
            elif x == oper[2]:
                stack.append(num1*num2)
            elif x == oper[3]:
                stack.append(num2/num1)
        else:
            stack.append(alphabet[x])
    print('%.2f' %stack[0])

solution()