# 22948번 : 원 이동하기 2 - Gold 3
import sys
from collections import deque
input = sys.stdin.readline

"""

"""

n = int(input())
circles = []
graph = [[] for _ in range(n+1)]
for _ in range(n):
    k, x, r = map(int, input().split())
    circles.append((k, x-r))
    circles.append((k, x+r))
circles.sort(key = lambda x : x[1])
A, B = map(int, input().split())
stack = [0]
circles.append((0, circles[-1][1] + 1))

for k, radius in circles:
    if stack[-1] != k:
        graph[k].append(stack[-1])
        graph[stack[-1]].append(k)
        stack.append(k)
    else:
        stack.pop()
visited = [False] * (n+1)

que = [[A]]
while que:
    node = []
    for _ in range(len(que)):
        cur_node = que.pop(0)
        last = cur_node[-1]
        if last == B:
            answer = cur_node
            break
        for num in graph[last]:
            if not visited[num]:
                visited[num] = True
                node.append(cur_node + [num])
    que = node

print(len(answer))
print(*answer)