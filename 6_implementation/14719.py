# 14719번 : 빗물 - Gold 5
import sys
input = sys.stdin.readline
"""
빗물이 고이는 조건이 무엇일까?
약간 양의 2차함수처럼 숫자의 흐름이 낮아지다가 상승하는 그런 부분에서 빗물이 고인다.
    예를 들어 2 3 1 2 3 4 가 있으면 3부터 4까지 부분에 물이 고이는 것.
"""

h, w = map(int, input().split())
world = list(map(int, input().split()))

ans = 0
for i in range(1, w - 1):
    left_max = max(world[:i])
    right_max = max(world[i+1:])

    compare = min(left_max, right_max)

    if world[i] < compare:
        ans += compare - world[i]

print(ans)