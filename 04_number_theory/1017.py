import sys

input = sys.stdin.readline
INF = sys.maxsize
'''
    https://www.acmicpc.net/problem/1017
'''


def dfs(x):
    global Y
    global matched
    global visited
    if visited[Y.index(x)]: return False
    visited[Y.index(x)] = True
    for y in Y:
        if prime[x + y]:
            if y not in matched or dfs(matched[y]):
                matched[y] = x
                return True
    return False


prime = [True] * 2002
for i in range(2, int(2001 ** 0.5)):
    if prime[i]:
        for j in range(i + i, 2001, i):
            prime[j] = False

N = int(input())
X = list(map(int, input().split()))
answers = []
even = []
odd = []
for i in answers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
if len(even) != len(odd):
    print(-1)
else:
    for i in X:
        matched = {}
        if i == X[0]: continue
        if prime[X[0] + i]:
            if N == 2:
                answers.append(i)
                break
            Y = [x for x in X]
            del Y[0]
            del Y[Y.index(i)]
            matched = {}
            for y in Y:
                visited = [False for _ in range(len(Y))]
                dfs(y)

        if N != 2 and len(matched) == N - 2: answers.append(i)

    if not answers:
        answers.append(-1)
    answers.sort()
    print(' '.join(list(map(str, answers))))
