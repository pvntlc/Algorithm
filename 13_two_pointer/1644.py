#1644번 : 소수의 연속합 – Gold 3
import sys
input = sys.stdin.readline

n = int(input())
a = [False, False] + [True] * (n-1)
primes = []

for i in range(2,n+1):
    if a[i]:
        primes.append(i)
        for j in range(i*i, n+1, i):
            a[j] = False

left, right = 0, 0
sum = 2
count = 0
while(True):
    if(sum < n):
        right += 1
        if (right == len(primes) or left == len(primes)):
            break
        sum += primes[right]
    elif(sum > n):
        if (right == len(primes) or left == len(primes)):
            break
        sum -= primes[left]
        left += 1
    else:
        count += 1
        right += 1
        if (right == len(primes) or left == len(primes)):
            break
        sum += primes[right]
        sum -= primes[left]
        left += 1

print(count)