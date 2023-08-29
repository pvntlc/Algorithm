# 2212번 : 센서 - Gold 5
import sys
input = sys.stdin.readline
INF = sys.maxsize
'''

'''

n = int(input())
k = int(input())
xy_list = sorted(list(map(int, input().split())))
answer_list = []
for i in range(len(xy_list)-1):
    answer_list.append(xy_list[i+1] - xy_list[i])
answer_list.sort(reverse=True)
print(sum(answer_list[k-1:]))
