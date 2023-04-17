#9095번 : 1, 2, 3 더하기 – Silver 3
import sys
input = sys.stdin.readline

T = int(input())
Dp = [0] * 11
Dp[0] = 1
Dp[1] = 1
Dp[2] = 2
for i in range(3,11):
    Dp[i] = Dp[i-1]+Dp[i-2]+Dp[i-3]

for i in range(T):
    num = int(input())
    print(Dp[num])