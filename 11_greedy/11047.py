# 11047번 :동전 0 - Silver 4
import sys
input = sys.stdin.readline
INF = sys.maxsize
'''
- N 종류의 동전을 무한히 가지고 있을 때, 적절히 사용해서 가치의 합을 K로 만든다.
- 필요한 동전 개수의 최솟값을 구하는 문제
- N 종류 동전의 가치는 오름차순으로 주어진다.
- **++ 동전의 가치는 반드시 배수로 주어진다.**
'''
n, k = map(int, input().split())
price = []
for _ in range(n):
    price.append(int(input()))

answer = k
idx = n-1
real_answer = 0
while answer != 0:
    mock = answer // price[idx]
    answer -= mock * price[idx]
    idx -= 1
    real_answer += mock
print(real_answer)