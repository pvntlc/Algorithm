import sys
from itertools import combinations
input = sys.stdin.readline


'''

'''


n = int(input())
answer = []
for i in range(1,11):
    for num in combinations(range(0,10), i):
        temp = list(num)
        temp.sort(reverse=True)
        answer.append(int("".join(map(str, temp))))
answer.sort()
if n <= 1022:
    print(answer[n])
else:
    print(-1)
