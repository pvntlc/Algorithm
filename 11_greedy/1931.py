# 1931번 : 회의실 배정 - Silver 1
import sys
input = sys.stdin.readline
INF = sys.maxsize
'''
- 전형적인 그리디 알고리즘 문제.
- 회의가 끝나는 시간을 기준으로 오름차순으로 정렬한다.
- 그 후 회의 시작 시간과 끝나는 시간이 겹치지 않도록 배정해주면 된다.
- 회의실이 1개밖에 없기 때문에 간단하게 풀 수 있다.
'''

n = int(input())
time = []
for _ in range(n):
    time.append(tuple(map(int, input().split())))
time.sort(key=lambda x:(x[1], x[0]))

end_time = time[0][1]
value = 1
for i in range(1,n):
    start_time = time[i][0]

    if end_time <= start_time:
        end_time = time[i][1]
        value += 1
print(value)