# 11399번 : ATM - Silver 4
import sys
input = sys.stdin.readline
INF = sys.maxsize
'''

'''

n = int(input())
time = list(map(int, input().split()))
time.sort()
answer = 0

for i in range(n):
    subtotal = sum(time[0:i+1])
    answer += subtotal
print(answer)