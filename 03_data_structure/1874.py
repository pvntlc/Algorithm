# 1874번 : 스택 수열 - Silver 2
import sys
input = sys.stdin.readline
"""

"""
def solution():
    n = int(input())
    stack = []
    count = 1 #넣을수
    answer = []
    for i in range(n):
        num = int(input())
        while count <= num:
            stack.append(count)
            answer.append("+")
            count += 1
        if stack[-1] == num:
            stack.pop()
            answer.append("-")
        else:
            answer = ["NO"]
            break
    print('\n'.join(answer)) #join을 애용하자. *answer보다 거의 두배는 빠른듯함?
solution()