import sys


input = sys.stdin.readline


def solve():
    n = int(input())
    answer = [10] + [0 for _ in range(1000)]
    scores = [list(map(int, input().split())) for _ in range(n)]
    scores.sort(key=lambda x : (-x[1],x[0]))

    for x,y in scores:
        for i in range(x,0,-1):
            if answer[i] == 0:
                answer[i] = y
                break

    print(sum(answer)-10)

solve()