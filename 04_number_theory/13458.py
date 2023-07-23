# 13458번 : 시험 감독 - Bronze 2
import sys
input = sys.stdin.readline
INF = sys.maxsize
'''
https://www.acmicpc.net/problem/13458

1. 총 n개의 시험장이 있고, i번 시험장에 있는 응시자의 수는 Ai이다.
2. 총감독관과 부감독관이 있으며, 총감독관은 B명 부감독관은 C명을 감독할 수 있다.
3. 각각의 시험장에 총감독관은 오직 1명, 부감독관은 여러 명 필요하다.
'''

n = int(input())
students = list(map(int, input().split()))
b_sup, c_sup = map(int, input().split())

ans = 0

for i in range(n):
    if students[i] <= b_sup:
        ans += 1
    elif (students[i] - b_sup) % c_sup == 0:
        ans += ((students[i] - b_sup) // c_sup) + 1
    else:
        ans += ((students[i] - b_sup) // c_sup) + 2

print(ans)