# 2960번 : 에라토스테네스의 체– Silver 4
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
num = [1] * (n + 1)

for i in range(2, n + 1):
    if num[i] == 0: continue
    if k == 0: break

    for j in range(i, n + 1, i):
        if num[j]:
            num[j] = 0
            k -= 1
        if k == 0:
            print(j)
            break