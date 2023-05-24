# 20164번 : 홀수 홀릭 호석 - Gold 5
import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize
"""
"""
answer = [INF, -INF]


def count_odds(x):
    cnt = 0
    for char in x:
        if char in '13579':
            cnt += 1
    return cnt


def cal(x,cur):
    if len(x) == 1:
        answer[0] = min(count_odds(x) + cur, answer[0])
        answer[1] = max(count_odds(x) + cur, answer[1])
        return

    elif len(x) == 2:
        cal(str(int(x[0]) + int(x[1])), cur + count_odds(x))

    else:
        odds = count_odds(x)
        for i in range(1, len(x) - 1):
            for j in range(i + 1, len(x)):
                cal(str(int(x[:i]) + int(x[i:j]) + int(x[j:])), cur + odds)

x = input().rstrip()
cal(x, 0)
print(*answer, sep=' ')
