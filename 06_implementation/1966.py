# 1700번 : 멀티탭 스케줄링 - Gold 1
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

'''
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
'''

for _ in range(int(input())):
    n, m = map(int, input().split()) #n개의 숫자가 들어오고, m번째가 몇번째인지..
    count = 0
    priority = []
    values = list(map(int, input().split()))

    for i in values:
        priority.append((i, count))
        count += 1

    count = 0
    while priority:
        x,y = priority.pop(0)
        if x == max(values):
            values[y] = -1
            count += 1
            if y == m:
                print(count)
                break
        else:
            priority.append((x,y))