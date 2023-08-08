# 1339번 : 단어 수학 - Gold 4
import sys
from collections import defaultdict

input = sys.stdin.readline

'''

'''
n = int(input())
n_dict = defaultdict(int)
answer = []
for _ in range(n):
    temp = list(input().rstrip())
    answer.append(temp)
    idx = 10 ** len(temp)
    for i in range(len(temp)):
        n_dict[temp[i]] += idx
        idx //= 10

n_dictt = sorted(n_dict.items(), key = lambda x : x[1], reverse=True)
idx = 9

for i in n_dictt:
    x,y = i
    n_dict[x] = idx
    idx -= 1

result = 0

for i in answer:
    temp = ""
    for k in i:
        temp += str(n_dict[k])
    result += int(temp)

print(result)