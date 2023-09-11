import sys
import heapq as hq
from collections import deque
input = sys.stdin.readline


'''

'''

n,l = map(int, input().split())
n_list = list(map(int, input().split()))
answer = []
que = deque()
que.append((0,n_list[0]))
print(que[0][1],end=" ")
for i in range(1,n):

    if que[0][0] + l <= i:
        que.popleft()

    if len(que) == 0:
        que.append((i,n_list[i]))
        print(que[0][1],end=" ")
        continue

    if que[-1][1] > n_list[i]:
        while len(que) >= 1 and que[-1][1] >= n_list[i]:
            que.pop()
        que.append((i,n_list[i]))
    else:
        que.append((i, n_list[i]))
    print(que[0][1], end=" ")