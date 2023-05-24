# 2637번 : 장난감 조립 - Gold 2
import sys
from collections import deque
input = sys.stdin.readline
INF = (10)**5+1
"""
문제

건물을 짓는 데에는 초가 걸리며, 동시에 여러 개의 자원을 만들거나 건물을 지을 수 있다.
"""
def t_sort(already_built, resource, graph, indegree, n,t):
    que = deque()
    answer = []
    visited = [False] * (n+1)

    for x in already_built:
        que.append((0,x))

    while que:
        time, num = que.popleft()

        if time > t:
            break

        for i in resource[num]:
            if visited[i]:
                continue
            visited[i] = True
            for j in graph[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    que.append((time + 1, j))
        answer.append(num)

    return answer


def solution():
    n,m,t = map(int, input().split()) #자원의 가짓수, 지어진 건물의 개수, 제한 시간
    already_built = list(map(int, input().split())) #이미 지어진 건물
    resource = [0]
    graph = [[] for _ in range(n+1)] #1번 자원이 있으면 2,5번 건물을 지을 수 있다.
    indegree = [0] * (n+1)

    for i in range(1, n + 1):
        resource.append(list(map(int, input().split()[1:])))

    for _ in range(n-m): # 아직 지어지지 않은 건물과 건물마다 필요로 하는 자원의 가짓수.
        line = list(map(int, input().split()))
        indegree[line[0]] = line[1]
        for i in range(line[1]):
            graph[line[i+2]].append(line[0])

    answer = t_sort(already_built, resource, graph, indegree, n,t)
    print(len(answer))
    answer.sort()
    print(*answer)
solution()