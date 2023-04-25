#1021번 : 회전하는 큐 - Silver 3
import sys
from collections import deque
input = sys.stdin.readline
"""
10 3
2 9 5
>>
1 2 3 4 5 6 7 8 9 10
2 3 4 5 6 7 8 9 10 1 //
3 4 5 6 7 8 9 10 1
1 3 4 5 6 7 8 9 10
10 1 3 4 5 6 7 8 9 
9 10 1 3 4 5 6 7 8  //
10 1 3 4 5 6 7 8 


"""
def cal_2(que, num):
    global count
    while que[0] != num:
        n = que.popleft()
        que.append(n)
        count += 1
    que.popleft()

def cal_3(que, num):
    global count
    while que[0] != num:
        n = que.pop()
        que.appendleft(n)
        count +=1
    que.popleft()

n,m = map(int, input().split())
que = deque(i for i in range(1,n+1))
case = list(map(int, input().split()))
count = 0

for i in range(m):
    idx = 0
    num = case[i]
    for j in range(len(que)):
        if num == que[j]:
            idx = j
            break
    if idx <= len(que)//2:
        cal_2(que, num)
    else:
        cal_3(que, num)

print(count)