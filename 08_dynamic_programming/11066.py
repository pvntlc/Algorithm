# 11066번 : 파일 합치기 - Gold 3
import sys
input = sys.stdin.readline
INF = sys.maxsize
'''

'''
for _ in range(int(input())):
    n = int(input())
    n_list = [0] + list(map(int, input().split()))
    c_sum = [0] * (n+1)
    for i in range(1,n+1):
        c_sum[i] = c_sum[i-1] + n_list[i]
    DP = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(2, n+1):
        for j in range(1, n-i+2):
            DP[j][i+j-1] = min([DP[j][j+k] + DP[j+k+1][j+i-1] for k in range(i-1)]) + c_sum[i+j-1] - c_sum[j-1]

    print(DP[1][n])