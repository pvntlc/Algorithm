# 16563번 : 어려운 소인수분해 – Gold 4
import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
"""
- N개의 자연수 k를 소인수분해하여 소인수들을 오름차순으로 출력하는 문제.
- N의 범위가 1,000,000까지이므로, 시간복잡도에 대한 신경을 많이 써줘야 하는 문제이다.
- 처음에는 에라토스테네스의 체로 소수의 리스트를 구하고, 그 리스트를 반복문을 통해 나누면서 출력하려고 했었다.
- 그러나 당연히 시간 초과가 났고, 애초에 에라토스테네스의 체를 통해서 소수를 구할 때, 그 과정에서 가장 작은 소인수를 저장해두면 좋을 것 같다는 생각이 들었다.
- 반복문을 통해서 answer 리스트에 저장해서 한번에 출력하려고 했으나, 이것도 시간초과가 났다.
- 그래서 while문이 돌아갈 때마다 바로 출력할 수 있도록 수정하였다.
"""
def is_Prime(n):
    isPrime = [1] * (n+1)
    isPrime[0] = isPrime[1] = 0

    for i in range(int(n**0.5)+1):
        if isPrime[i] == 1:
            for j in range(i*i, n+1, i):
                if isPrime[j] == 1:
                    isPrime[j] = i

    return isPrime

def solution():
   n = int(input())
   n_list = list(map(int, input().split()))
   prime_list = is_Prime(max(n_list))

   for i in n_list:
       while prime_list[i] != 1:
            print(prime_list[i], end=" ")
            i = i // prime_list[i]
       print(i)
solution()