# 15686번 : 치킨 배달 - Gold 5
import sys
from itertools import combinations
input = sys.stdin.readline
INF = sys.maxsize
'''
https://www.acmicpc.net/problem/15686

1. 도시의 각 칸은 (빈 칸, 치킨집, 집) 중 하나이다.
2. 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리를 의미한다.
3. 도시의 치킨 거리는 모든 집의 치킨 거리의 합을 의미한다.
4. 도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집을 모두 폐업시켜야 함.
5. 이렇게 했을 때, 어떻게 고르면 도시의 치킨 거리가 가장 작게될지 구하는 문제.

N은 2이상, 50이하. M은 1이상 13이하.
0은 빈 칸, 1은 집, 2는 치킨 집을 의미한다.

입력
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

출력
5

'''
import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(n))
result = 999999
house = []      # 집의 좌표
chick = []      # 치킨집의 좌표

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chick.append([i, j])

for chi in combinations(chick, m):  # m개의 치킨집 선택
    temp = 0            # 도시의 치킨 거리
    for h in house:
        chi_len = 999   # 각 집마다 치킨 거리
        for j in range(m):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += chi_len
    result = min(result, temp)

print(result)