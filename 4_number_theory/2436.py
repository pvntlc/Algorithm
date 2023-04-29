# 2436번 : 공약수 – Gold 5
import sys
import itertools
input = sys.stdin.readline
"""

"""
def gcdIter(a,b):
    if a<b:
        a,b = b,a
    while b:
        a,b = b, a%b
    return a

def divisor(n,g):
    for i in range(int(n**0.5)+1,0,-1):
        if n % i == 0 and gcdIter(i, n // i) == 1:
            a = i*g
            b = n // i * g
            if a > b:
                print(b,a)
            else:
                print(a,b)
            return


def solution():
    a,b = map(int,input().split())
    divisor(b//a,a)


solution()