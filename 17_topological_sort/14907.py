#14907번 : 프로젝트 스케줄링 - Gold 2
import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

"""

"""
def t_sort(time, inDegree, graph):
    que = deque()
    answer = 0
    dp = time[:]

    for i in range(26):
        if inDegree[i] == 0:
            que.append(i)

    while que:
        node = que.popleft()
        answer = max(answer, dp[node])

        for next in graph[node]:
            inDegree[next] -= 1
            if inDegree[next] == 0:
                que.append(next)
            dp[next] = max(dp[next], dp[node] + time[next])

    return answer

def solution():
    lines = sys.stdin.readlines()
    inDegree = [0] * 26
    time = [0] * 26
    graph = [[] for _ in range(26)]

    for line in lines:
        line = line.split()
        num = ord(line[0]) - ord('A')
        time[num] = int(line[1])

        if len(line) == 2:
            continue

        inDegree[num] = len(line[2])

        for cha in line[2]:
            cha_num = ord(cha) - ord('A')
            graph[cha_num].append(num)

    print(t_sort(time, inDegree, graph))
solution()