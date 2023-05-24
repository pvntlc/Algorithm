# 2609번 : 최대공약수와 최소공배수 - Silver 5
import sys
input = sys.stdin.readline

def gcdIter(a,b):
    while b:
        a,b = b,a%b
    return a

def lcmIter(a,b):
    return int(a * b / gcdIter(a,b))

def solution():
    num1, num2 = map(int, input().split())
    if num1 < num2:
        num1, num2 = num2, num1
    print(gcdIter(num1, num2))
    print(lcmIter(num1, num2))
solution()