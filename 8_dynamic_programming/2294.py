# 2294번 : 동전 2 - Gold 5
import sys
input = sys.stdin.readline
INF = sys.maxsize
'''
- N 종류의 동전을 무한히 가지고 있을 때, 적절히 사용해서 가치의 합을 k로 만드는 문제
- 필요한 동전 개수의 최솟값을 구하는 문제
- 11047번과 다른 점은, 동전의 가치가 배수로 주어지지 않는다는 것.
- 때문에, dp를 활용해서 문제를 푼다.
'''
n, k = map(int, input().split())
price = []
for _ in range(n):
    price.append(int(input()))

dp = [10001] * (k+1)
dp[0] = 0

for num in price:
   for i in range(num, k+1):
       dp[i] = min(dp[i],dp[i-num]+1)
if dp[k] == 10001:
   print(-1)
else:
   print(dp[k])