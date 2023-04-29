# 14490번 : 백대열 – Silver 4
import sys
input = sys.stdin.readline
"""

"""
def gcd_iter(a,b):
    if a < b:
        b,a = a,b
    while(b):
        a,b = b, a%b
    return a

def solution():
    a,b = map(int, input().rstrip().split(":"))
    n = gcd_iter(a,b)
    print(a//n,":",b//n,sep="")

solution()