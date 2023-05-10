# 1744번 : 수 묶기 - Gold 4
import sys
from collections import deque
input = sys.stdin.readline
"""
문제
1. 음수 양수를 따로 받아서 배열을 만든다.
2. 양수는 그냥 정렬, 음수는 역정렬한다.
3. 
"""
def solution():
    plus_list = []
    minus_list = []
    cal = []
    sum = 0
    n = int(input())

    for _ in range(n):
        number = int(input())

        if number > 0:
            plus_list.append(number)
        else:
            minus_list.append(number)

    plus_list.sort(reverse=True)
    minus_list.sort()
    print(plus_list)
    print(minus_list)
    for num in plus_list:
        if num == 1:
            sum += 1
            continue
        if not cal:
            cal.append(num)
            continue
        sum += cal[0] * num
        cal = []
    if cal:
        sum += cal[0]
        cal = []

    for num in minus_list:
        if not cal:
            cal.append(num)
            continue
        sum += cal[0] * num
        cal = []

    if cal:
        sum += cal[0]
        cal = []

    print(sum)


solution()