import sys
from collections import Counter
input = sys.stdin.readline

def solution():
    text = input().rstrip()
    text_dict = dict()

    for t in text:
        if t in text_dict:
            text_dict[t] += 1
        else:
            text_dict[t] = 1

    flag = 0
    mid_text = ""
    answer = []
    for t in sorted(text_dict.keys()):
        quo = text_dict[t] // 2
        rem = text_dict[t] % 2
        if rem == 1:
            if flag == 0:
                mid_text = t
                flag = 1
            else:
                flag = 2
                break
        if quo > 0:
            for _ in range(quo):
                answer.append(t)
    if flag == 2:
        print("I'm Sorry Hansoo")
        return
    print(*answer,mid_text,*answer[-1::-1],sep="")
solution()