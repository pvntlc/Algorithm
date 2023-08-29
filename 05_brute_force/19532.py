# 19532번 : 수학은 비대면강의입니다 - Bronze 2
import sys
input = sys.stdin.readline

"""
1 3 -1 4 1 7
2 -1
"""
coef = list(map(int, input().split()))
for x in range(-999, 1000):
    for y in range(-999, 1000):
        answer1 = coef[0] * x + coef[1] * y
        answer2 = coef[3] * x + coef[4] * y

        if answer1 == coef[2] and answer2 == coef[5]:
            print(x,y)
            break
