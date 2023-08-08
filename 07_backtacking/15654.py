import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def n_m():
    if len(answer) == m:
        print(' '.join(map(str,answer)))
        return

    for i in numbers:
        if not i in answer:
            answer.append(i)
            n_m()
            answer.pop()
    return


n,m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
answer = []
n_m()