import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def n_m(start):
    if len(answer) == m:
        print(' '.join(map(str,answer)))
        return

    for i in range(start, n):
        if not numbers[i] in answer:
            answer.append(numbers[i])
            n_m(i+1)
            answer.pop()
    return


n,m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
answer = []
n_m(0)
