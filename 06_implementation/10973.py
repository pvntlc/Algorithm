# 10973번 : 이전 순열 - Silver 3
import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
a = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    if a[i] < a[i-1]:
        x, y = i-1, i
        for j in range(N-1, 0, -1):
            if a[j] < a[x]:
                a[j], a[x] = a[x], a[j]
                a = a[:i] + sorted(a[i:], reverse=True)
                print(*a)
                exit(0)
print(-1)