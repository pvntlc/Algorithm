# 10804번 : 카드 역배치 - Bronze 2
import sys
input = sys.stdin.readline
INF = (10)**5+1
"""
"""
n_list = [i for i in range(0,21)]
for _ in range(10):
    a,b = map(int, input().split())
    n_list[a:b+1] = n_list[b:a-1:-1]


print(*n_list[1:])