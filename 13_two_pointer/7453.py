# 7453번 : 합이 0인 네 정수
import sys
from collections import defaultdict
input = sys.stdin.readline
INF = sys.maxsize

'''
1. 배열이 1개, 2개일 경우에는 똑같이 투포인터
2. 배열이 3개인 경우에는 하나를 고정시켜놓고 투포인터.
3. 배열이 4개인 경우에는 다음과 같이 두개의 배열을 하나의 합으로 구해 총 2개의 배열로 만들기.
- 그러고 나서 일반적으로 start, end를 진행하는데, 같은 합이 존재할 경우가 있음.
- 그런 경우에는 while문 사용해서 다음과 같이 해결.
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
        while next_end >= 0 and cd[end] == cd[next_end]:
            next_end -= 1
        answer += (next_start - start) * (end - next_end)
        start, end = next_start, next_end

print(answer)