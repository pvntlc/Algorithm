# 13975번 : 파일 합치기 3 - Gold 4
import sys
import heapq as hq

input = sys.stdin.readline
INF = sys.maxsize
'''
- 1 20 2 3이라는 파일 크기를 가진 파일들이 있다면,
    1. 먼저 1 2 3 20으로 정렬한다.
    2. 앞에 있는 숫자들부터 합친다. 그래야 최소 비용이 되기 때문이다.
    3. 3 3 20 → 6 20 → 26이 된다.
    4. 따라서 최소 파일 비용은 3 + 6 + 26 = 35이다.
    5. 때문에 이건 그리디 풀이로 작성될 수 있다.
'''
for _ in range(int(input())):
    n = int(input())
    answer = 0
    n_list = list(map(int, input().split()))
    hq.heapify(n_list)

    while len(n_list) != 1:
        temp = hq.heappop(n_list) + hq.heappop(n_list)
        answer += temp
        hq.heappush(n_list, temp)

    print(answer)