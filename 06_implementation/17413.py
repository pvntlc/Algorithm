# 17413번 : 단어 뒤집기 2 - Silver 3
import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

temp = ""
flag = True
for text in input().rstrip() + " ":
    if text == " ":
        if flag:
            print(*temp[::-1],sep="",end=" ")
            temp = ""
        else:
            temp += " "
    elif text == "<":
        print(*temp[::-1],sep="",end="")
        temp = "<"
        flag = False
    elif not flag and text == ">":
        temp += ">"
        print(*temp,sep="",end="")
        temp = ""
        flag = True
    else:
        temp += text