# 1707번 : 이분 그래프 - Gold 4
import sys
input = sys.stdin.readline
INF = sys.maxsize
'''
https://www.acmicpc.net/problem/1707
1. 빌딩은 총 N개가 있다.
2. 

입력
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2

출력
YES
NO
'''

def bfs(start, group):
    que = [start]
    visited[start] = group
    while que:
        x = que.pop(0)

        for i in graph[x]:
            if not visited[i]:
                que.append(i)
                visited[i] = -1 * visited[x]
            elif visited[i] == visited[x]:
                return False
    return True


for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [False] * (v+1)

    for i in range(e):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)

    for i in range(1, v+1):
        if not visited[i]:
            result = bfs(i,1)
            if not result:
                break
    print('YES' if result else 'NO')
