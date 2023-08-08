import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def n_m(n,count,start):
    if count == m:
        print(' '.join(map(str,answer)))
        return

    for i in range(start,n+1):
        answer.append(i)
        n_m(n, count+1,i)
        answer.pop()
    return


n,m = map(int, input().split())
answer = []
n_m(n,0,1)