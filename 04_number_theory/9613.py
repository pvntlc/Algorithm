# 9613번 : GCD 합– Silver 3
import sys
input = sys.stdin.readline

"""

"""
def gcdIter(a,b):
    while b:
        a,b = b,a%b
    return a

def solution():
    for i in range(int(input())):
        sum = 0
        n_list = list(map(int, input().split()))
        for j in range(1,n_list[0]+1):
            for k in range(j+1, n_list[0]+1):
                sum += gcdIter(n_list[j], (n_list[k]))
        print(sum)
solution()