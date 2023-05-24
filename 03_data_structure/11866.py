# 11866번 : 요세푸스 문제 0 - Silver 5
import sys
from collections import deque

input = sys.stdin.readline
"""

"""


def solution():
    n, k = map(int, input().split())
    que = [i + 1 for i in range(n)]
    idx = 0
    answer = []

    while que:
        idx += k - 1
        if len(que) == 0:
            break
        idx %= len(que)
        answer.append(str(que.pop(idx)))

    # join메소드는 광장히 유용합니다. iterable 객체에 담긴 string들을 사이에 ', '로 이어 리턴하는 함수입니다.
    print('<' + ', '.join(answer) + '>')


solution()