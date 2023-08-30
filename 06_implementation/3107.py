# 3107번 : IPv6
import sys
input = sys.stdin.readline
INF = sys.maxsize
'''
https://www.acmicpc.net/problem/3107
'''

ip = input().rstrip().split(":")
cnt = 0
index = 0
for i in range(len(ip)):
    if ip[i] == '' and cnt == 0:
        cnt += 1
        index = i
    elif ip[i] == '' and cnt == 1:
        cnt += 1
    elif len(ip[i]) != 4:
        text = ip[i]
        while len(text) != 4:
            text = "0" + text
        ip[i] = text

if cnt == 1:
    del ip[index]
    number = 8 - len(ip)
    for _ in range(number):
        ip.insert(index, '0000')

elif cnt == 2:
    del ip[index]
    del ip[index]
    number = 8 - len(ip)
    for _ in range(number):
        ip.insert(index, '0000')

for i in range(len(ip)):
    if ip[i] == '' and cnt == 0:
        cnt += 1
        index = i
    elif ip[i] == '' and cnt == 1:
        cnt += 1
    elif len(ip[i]) != 4:
        text = ip[i]
        while len(text) != 4:
            text = "0" + text
        ip[i] = text

print(*ip, sep=":")
