# 12904번 : A와 B - Gold 5
import sys
input = sys.stdin.readline
INF = sys.maxsize
'''

'''

S = list(input().rstrip())
T = list(input().rstrip())

while len(T) != len(S):
    if T[-1] == "A":
        T.pop(-1)
    else:
        T.pop(-1)
        T = T[::-1]

if T == S:
    print(1)
else:
    print(0)