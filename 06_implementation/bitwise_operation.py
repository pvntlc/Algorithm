# 직사각형 좌표 구하기 - 카카오 코딩 테스트
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
"""
1,5,6,25
"""
def solution():
    v = [[1,4],[3,4],[3,10]]
    print(v[0][0] ^ v[1][0] ^ v[2][0])
    print(v[0][1] ^ v[1][1] ^ v[2][1])

solution()