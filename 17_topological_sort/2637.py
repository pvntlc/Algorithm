# 2637번 : 장난감 조립 - Gold 2
import sys
from collections import deque
input = sys.stdin.readline
"""
문제

"""
def bfs(n, n_list):
    que = deque()
    que.append(n)
    cnt = [0] * (n + 1)
    ans = [0] * (n + 1)

    cnt[n] = 1

    while que:
        node = que.popleft()

        if not n_list[node]:
            ans[node] += cnt[node]

        for x, count in n_list[node]:
            if not cnt[x]:
                que.append(x)
            cnt[x] += count * cnt[node]

        cnt[node] = 0
    return ans


def solution():
    n = int(input())
    n_list = [[] for _ in range(n+1)]
    m = int(input())

    for _ in range(m):
        a,b,c = map(int, input().split())
        n_list[a].append((b,c))
    ans = bfs(n,n_list)

    for i in range(1, n + 1):
        if ans[i]:
            print(i, ans[i])

solution()