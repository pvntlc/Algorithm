# 1027번 : 고층건물 - Gold 4
import sys
input = sys.stdin.readline
INF = sys.maxsize
'''
https://www.acmicpc.net/problem/1027

1. 빌딩은 총 N개가 있다.
2. 

입력
15
1 5 3 2 6 3 2 6 4 2 5 7 3 1 5

출력
7
'''
n = int(input())
n_list = list(map(int, input().split()))

answer = 0

for i in range(n):
    count = 0
    prev_temp = INF

    for j in range(i-1,-1,-1): # i기준 앞쪽
        temp = (n_list[i] - n_list[j]) / (i - j)
        if temp < prev_temp:
            count += 1
            prev_temp = temp

    prev_temp = -INF
    for j in range(i+1, n): # i기준 뒤쪽
        temp = (n_list[j] - n_list[i]) / (j - i)
        if temp > prev_temp:
            count += 1
            prev_temp = temp

    answer = max(answer, count)
print(answer)
