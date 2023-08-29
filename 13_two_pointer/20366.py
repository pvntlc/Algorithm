# 20306번 : 같이 눈사람 만들래? - Gold 3
import sys
input = sys.stdin.readline
INF = sys.maxsize

"""
"""

n = int(input())
n_list = sorted(list(map(int, input().split())))
min_value = INF
for i in range(n):
    for j in range(i+3,n):
        start = i+1
        end = j-1
        sum1 = n_list[i] + n_list[j]

        while start < end:
            sum2 = n_list[start] + n_list[end]
            if sum2 > sum1:
                min_value = min(abs(sum1-sum2), min_value)
                end -= 1
            elif sum2 < sum1:
                min_value = min(abs(sum1-sum2), min_value)
                start += 1
            else:
                print(0)
                exit(0)
print(min_value)