# 2531번 : 회전 초밥 - Silver 1
import sys
input = sys.stdin.readline
INF = sys.maxsize

"""
https://www.acmicpc.net/problem/2531

8 30 4 30
7
9
7
30
2
7
9
25

5
"""

n, d, k, c = map(int, input().split()) #접시의 수, 초밥의 가짓수, 연속해서 먹는 접시의 수, 쿠폰 번호
c_list = [int(input()) for _ in range(n)]
answer = dict()
answer[c] = 1

for i in range(k):
    if c_list[i] not in answer.keys():
        answer[c_list[i]] = 1
    else:
        answer[c_list[i]] += 1

max_value = len(answer)
for i in range(n):
    start = i
    end = (i + k) % (n)

    answer[c_list[start]] -= 1
    if answer[c_list[start]] == 0:
        del answer[c_list[start]]

    if c_list[end] not in answer.keys():
        answer[c_list[end]] = 1
    else:
        answer[c_list[end]] += 1
    max_value = max(len(answer), max_value)

print(max_value)