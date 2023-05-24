#1484번 : 다이어트 – Gold 5
import sys
import math
input = sys.stdin.readline

n = int(input())

def solution(n):
    left = 1
    right = 2
    count = 0
    while(left < right):
        sum = int(math.pow(right,2)) - int(math.pow(left,2))
        if sum > n:
            left += 1
        elif sum < n:
            right += 1
        else:
            print(right)
            left += 1
            right += 1
            count += 1
    if(count == 0):
        print(-1)

solution(n)