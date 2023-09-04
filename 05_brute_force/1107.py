# 1107번 : 리모컨 - Gold 5
import sys
input = sys.stdin.readline
INF = sys.maxsize

"""

"""
number = list(input().rstrip())
k = int(input())
xNumber = list(map(int,input().split()))
text =""
for i in range(len(number)):
    text += number[i]
answer = abs(int(text)-100) # 1. 그냥 클릭해서 이동

for i in range(1000001):
    num = str(i)
    for j in num:
        if int(j) in xNumber:
            break
    else:
        answer = min(answer, len(num) + abs(i-int(text)))
print(answer)