# 1783번 : 병든 나이트 - Silver 3
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

if n <= 1:
    print(1)
elif n == 2:
    if m < 3:
        print(1)
    elif m < 5:
        print(2)
    elif m < 7:
        print(3)
    else:
        print(4)
else:
    if m<= 1:
        print(1)
    elif m <= 4:
        print(m)
    elif m <= 6:
        print(4)
    else:
        print(m-2)
