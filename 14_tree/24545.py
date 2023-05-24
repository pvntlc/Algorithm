# 24545번 : Y - Platinum 5
import sys
input = sys.stdin.readline
from collections import deque
INF = sys.maxsize
'''
https://www.acmicpc.net/problem/24545

8
1 2
1 3
2 4
1 5
2 6
2 7
8 7

6
'''
n=int(input())
graph=[[] for _ in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

queue=deque([(1,0)])
visit=[0 for _ in range(n+1)]
m,p=0,1
while queue:
    a,d=queue.popleft()
    visit[a]=1
    if m<d:
        m,p=d,a
    for i in graph[a]:
        if visit[i]==0:
            queue.append((i,d+1))

parent=[0 for _ in range(n+1)]
visit=[0 for _ in range(n+1)]
m=0
queue=deque([(a,0)])
while queue:
    a,d=queue.popleft()
    visit[a]=1
    if m<d:
        m,p=d,a
    for i in graph[a]:
        if visit[i]==0:
            parent[i]=a
            queue.append((i,d+1))

dist=[10**9 for _ in range(n+1)]
queue=deque([])
while p!=0:
    queue.append((p,0))
    dist[p]=0
    p=parent[p]
ans=len(queue)

m=0
while queue:
    a,d=queue.popleft()
    dist[a]=d
    m=max(m,d)
    for i in graph[a]:
        if dist[i]==10**9:
            queue.append((i,d+1))

if m==0:
    print(0)
else:
    print(ans+m)