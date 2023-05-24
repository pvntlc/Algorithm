# 1759번 : 암호 만들기 - Gold 5
import sys
from itertools import combinations
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def isValid(x):
    vowels = ['a','e','i','o','u']
    count = 0
    for i in x:
        if i in vowels:
            count += 1
    return count >= 1 and len(x) - count >= 2
def solution():
    l,c = map(int, input().split())
    line = input().rstrip().split()
    line.sort()
    for x in combinations(line,l):
        if isValid(x):
            print(''.join(x))
solution()