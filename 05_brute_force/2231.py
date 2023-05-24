# 2231번 : 분해합 - Bronze 2
import sys
input = sys.stdin.readline

"""

"""
def solution():
    num = int(input())
    for i in range(1,1000001):
        line = str(i)
        sum = i

        for x in line:
            sum += int(x)
        if sum == num:
            print(i)
            return
    print(0)

solution()