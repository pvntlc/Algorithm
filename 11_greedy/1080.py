# 1080번 : 행렬 - Silver 1
import sys
import heapq as hq
input = sys.stdin.readline
INF = sys.maxsize
'''

'''
def reverse(x,y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            a[i][j] = 1 - a[i][j]

def check():
    for i in range(n):
        for j in range(m):
            if b[i][j] != a[i][j]:
                return False
    return True

n,m = map(int, input().split())

a = [list(map(int,list(input().rstrip()))) for _ in range(n)]
b = [list(map(int,list(input().rstrip()))) for _ in range(n)]

count = 0

for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            reverse(i,j)
            count += 1

if check():
    print(count)
else:
    print(-1)