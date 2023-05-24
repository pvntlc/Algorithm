# 2470번 : 두 용액 - Gold 5
import sys
input = sys.stdin.readline
INF = sys.maxsize

"""
"""

n = int(input())
n_list = list(map(int,input().split()))
left = 0
right = len(n_list)-1
answer = INF
n_list.sort()

while left != right:
    temp = n_list[left] + n_list[right]

    if abs(temp) < answer:
        answer = abs(temp)
        final = (n_list[left], n_list[right])

    if temp > 0:
        right -= 1
    elif temp == 0:
        break
    else:
        left += 1

print(*final)