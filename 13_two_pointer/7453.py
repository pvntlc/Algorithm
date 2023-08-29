# 7453번 : 합이 0인 네 정수
import sys
from collections import defaultdict
input = sys.stdin.readline
INF = sys.maxsize

'''

'''
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ab = []
cd = []

for i in range(n):
    for j in range(n):
        ab.append(arr[i][0]+arr[j][1])
        cd.append(arr[i][2]+arr[j][3])
ab.sort()
cd.sort()

start = 0
end = len(ab)-1
answer = 0

while True:
    if start == len(ab) or end == -1:
        break

    if ab[start] + cd[end] > 0:
        end -= 1

    elif ab[start] + cd[end] <0:
        start += 1
    else:
        next_start = start + 1
        next_end = end - 1

        while next_start < len(ab) and ab[start] == ab[next_start]:
            next_start += 1
        while next_end < len(cd) and cd[end] == cd[next_end]:
            next_end -= 1
        answer += (next_start - start) * (end - next_end)
        start, end = next_start, next_end

print(answer)