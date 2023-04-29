# 1436번 : 영화감독 숌 - Silver 5
import sys
input = sys.stdin.readline

"""

"""
def solution():
    num = int(input())
    count = 0
    for i in range(1,10000000):
        line = str(i)
        if '666' in line:
            count += 1

        if count == num:
            print(i)
            break

solution()