# 4803번 : 트리 – Gold 4
import sys
input = sys.stdin.readline
'''
https://www.acmicpc.net/problem/4803

6 3
1 2
2 3
3 4
6 5
1 2
2 3
3 4
4 5
5 6
6 6
1 2
2 3
1 3
4 5
5 6
6 4
0 0

Case 1: A forest of 3 trees.
Case 2: There is one tree.
Case 3: No trees.
'''
def DFS(prev, node):
    visited[node] = False
    for curr in n_list[node]:
        if curr == prev:
            continue
        if not visited[curr]:
            return False
        if not DFS(node, curr):
            return False
    return True

cnt = 0
while True:
    cnt += 1
    n, m = map(int, input().split())

    if n == 0 and m == 0: # 종료
        break

    n_list = [[] for _ in range(n+1)]
    visited = [True] * (n+1)

    for _ in range(m):
        start, end = map(int, input().split())
        n_list[start].append(end)
        n_list[end].append(start)

    count = 0
    for i in range(1, n+1):
        if visited[i]:
            if DFS(0,i):
                count += 1

    if count == 0:
        print("Case {}: No trees.".format(cnt))
    elif count == 1:
        print("Case {}: There is one tree.".format(cnt))
    else:
        print("Case {}: A forest of {} trees.".format(cnt, count))