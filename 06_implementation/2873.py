# 2873번 : 롤러코스터 - Platinum 3
import sys
input = sys.stdin.readline
INF = sys.maxsize
'''
https://www.acmicpc.net/problem/2873
'''

r, c = map(int, input().split())
number_list = [list(map(int, input().split())) for _ in range(c)]

if r % 2 == 1:
    print(('R' * (c - 1) + 'D' + 'L' * (c - 1) + 'D') * (r // 2) + 'R' * (c - 1))
elif c % 2 == 1:
    print(('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * (c // 2) + 'D' * (r - 1))

else:
    low = 1000
    position = [-1, -1]

    for i in range(r):
        if i % 2 == 0:
            for j in range(1, c, 2):
                if low > number_list[i][j]:
                    low = number_list[i][j]
                    position = [i, j]
        else:  # i % 2 == 1
            for j in range(0, c, 2):
                if low > number_list[i][j]:
                    low = number_list[i][j]
                    position = [i, j]

    res = ('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * (position[1] // 2)
    x = 2 * (position[1] // 2)
    y = 0
    xbound = 2 * (position[1] // 2) + 1

    while x != xbound or y != r - 1:
        if x < xbound and [y, xbound] != position:
            x += 1
            res += 'R'
        elif x == xbound and [y, xbound - 1] != position:
            x -= 1
            res += 'L'
        if y != r - 1:
            y += 1
            res += 'D'

    res += ('R' + 'U' * (r - 1) + 'R' + 'D' * (r - 1)) * ((c - position[1] - 1) // 2)

    print(res)