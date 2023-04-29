# 6588번 : 골드바흐의 추측 - Silver 1
import sys
input = sys.stdin.readline
"""

"""
NUM = 1000000

def is_prime(num):
    prime = [True] * (num+1)
    prime[0] = prime[1] = False
    answer = []

    for i in range(int(num**0.5)+1):
        if prime[i]:
            answer.append(i)
            for j in range(i**2, num+1, i):
                prime[j] = False
    return answer,prime

def solution():
    answer,prime = is_prime(NUM)

    while True:
        n = int(input())
        for x in answer:
            if prime[n-x]:
                print("%d = %d + %d" %(n,x,n-x))
                break
        if n == 0:
            break
solution()