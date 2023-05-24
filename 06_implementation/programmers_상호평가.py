# [프로그래머스/java] 상호 평가 - 네이버 코딩테스트(코테) 기출문제
import sys
from itertools import combinations
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def solution():
    scores = [[70,49,90],[68,50,38],[73,31,100]]
    same = []
    scores = list(map(list, zip(*scores)))
    for i in range(len(scores)):
        same.append(scores[i][i])

    max_count, min_count = 0,0
    for i in range(len(scores)):
        if scores[i][i] == max(same):
            max_count += 1
            max_index = i
        if scores[i][i] == min(same):
            min_count += 1
            min_index = i

    if max_count == 1:
        del scores[max_index][max_index]
    if min_count == 1:
        del scores[min_index][min_index]

    answer=[]
    for i in scores:
        grade = sum(i) / len(i)

        if grade >= 90:
            answer.append('A')
        elif grade >= 80:
            answer.append('B')
        elif grade >= 70:
            answer.append('C')
        elif grade >= 50:
            answer.append('D')
        else:
            answer.append('F')

    print(''.join(answer))

solution()