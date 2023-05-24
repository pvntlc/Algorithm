import sys
import heapq
"""
- 일단 이 문제는 우선순위큐가 섞인 문제로, 사실 정렬보다는 우선순위큐와 관련된 문제라고 볼 수 있겠다.
- 이 문제를 처음 보고 나서 우선순위큐로 풀어야겠다는 생각을 못해서 많이 헤맸었는데, 관련 알고리즘에 우선순위큐가 있는 것을 보고 그 쪽으로 코드를 작성했다.
- 우선, 집과 사무실의 위치가 크기 순으로 정렬된 것이 아니기 때문에 집과 사무실의 위치를 크기 순으로 정렬한다. 출발과 도착지로 바꾼다고 생각하면 된다.
- 그 후에는 도착지를 기준으로 정렬해준다. 우리는 도착지를 기준으로 d를 뺐을 때 출발지가 그 안에 있으면 포함할 것이기 때문이다.
"""

n = int(sys.stdin.readline())
houses = []
for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    if start > end:  # 출발지와 도착지를 바꿔줌
        start, end = end, start
    houses.append((start, end))

d = int(sys.stdin.readline())
houses.sort(key=lambda x: x[1])  # 도착지 기준으로 오름차순 정렬

heap = []  # 출발지점을 저장할 최소힙
max_count = 0
for house in houses:
    start, end = house
    if end - start <= d:  # 선로 길이보다 짧은 집들만 골라서 최소힙에 추가
        heapq.heappush(heap, start)
        while heap and end - heap[0] > d:  # 선로 길이보다 큰 집은 최소힙에서 제거
            heapq.heappop(heap)
        max_count = max(max_count, len(heap))  # 최대 집의 개수 갱신

print(max_count)