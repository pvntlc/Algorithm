# 20442번 : ㅋㅋ루ㅋㅋ - Gold 2
import sys
input = sys.stdin.readline
INF = sys.maxsize

'''
1. 양쪽 끝의 문자열이 같은지 판단한다.
2. 같을 경우에 전의 문자가 r이면 카운트x.
3. 다른 경우에는 k쪽을 버림.
'''

text = list(input().rstrip())

start = 0
end = len(text)-1
answer = 0
while start <= end:
    if start == end:
        if text[start] == "R":
            answer += 1
        break

    elif text[start] == text[end]:
        if text[start] == "K":
            if start - 1 >= 0 and text[start-1] == "K":
                answer += 2
            elif start == 0:
                answer += 2
            elif start - 1 >= 0 and text[start-1] == "R" and text[end+1] == "R":
                answer += 2
        else:
            answer += 2
        start += 1
        end -= 1

    else:
        if text[start] == "K":
            start += 1
            answer += 1
        else:
            end -= 1
            answer += 1
print(answer)
