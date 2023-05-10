# 1541번 : 잃어버린 괄호 - Silver 2
import sys
input = sys.stdin.readline
INF = sys.maxsize
'''

'''
exp = input().rstrip().split('-')
num = []
for i in exp:
    cnt = 0
    sum = i.split('+')
    for j in sum:
        cnt += int(j)
    num.append(cnt)
ans = num[0]
for i in range(1, len(num)):
    ans -= num[i]
print(ans)