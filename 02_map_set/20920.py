# 20920번 : 영단어 암기는 괴로워 – Silver 3
import sys
import math
import itertools
from collections import Counter
input = sys.stdin.readline
INF = (10)**5+1
"""

"""
def solution():
    n, m = map(int, input().split())
    word_dict = dict()
    for i in range(n):
        word = input().rstrip()
        if len(word) < m:
            continue

        if not word in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    answer = list(word_dict.keys())
    answer.sort(key = lambda x : (-word_dict[x], -len(x), x))
    print(*answer, sep="\n")
solution()