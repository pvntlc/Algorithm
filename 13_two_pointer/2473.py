#2473번 : 세 용액 - Gold 3
import sys
input = sys.stdin.readline
'''
이중 포인터로 풀지만, 가장 작은 값은 고정해둔 상태에서 풀면 된다.
'''

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
INF = sys.maxsize

def find_liquid(n, arr):
    min_diff = INF
    ans = []

    for fixed in range(n-2):
        p1 = fixed + 1
        p2 = n - 1

        while p1 < p2:
            mixed = arr[p1] + arr[p2] + arr[fixed]
            if mixed == 0:
                return [arr[fixed], arr[p1], arr[p2]]

            if abs(mixed) < min_diff:
                ans = [arr[fixed], arr[p1], arr[p2]]
                min_diff = abs(mixed)

            if mixed < 0:
                p1 += 1
            else:
                p2 -= 1

    return ans


print(*find_liquid(N, arr))