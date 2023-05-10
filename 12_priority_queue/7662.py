# 7662번 : 이중 우선순위 큐 - Gold 4 ***
import sys
import heapq as hq
input = sys.stdin.readline
INF = sys.maxsize
'''
1. 할때마다 heapify 계속 하는 거임. -> 요거는 내 생각에 시간복잡도 엄청 늘어날 것 같은데?
2. 그게 아니면 최소 힙이랑 최대 힙이랑 나눠서 실행하는 거임. -> 얘는 최대값 삭제할 때 최소힙에서 어떻게 삭제함??
-> 
'''
def remove_invalid_data(heap):
    while heap and not is_valid[heap[0][1]]:
        hq.heappop(heap)
    return

for _ in range(int(input())):
    min_heap = []
    max_heap = []
    is_valid = []
    idx = 0

    for _ in range(int(input())):
        cmd, num = input().split()

        if cmd == "D":
            if int(num) == 1:
                remove_invalid_data(max_heap)
                if max_heap:
                    is_valid[hq.heappop(max_heap)[1]] = False
            else:
                remove_invalid_data(min_heap)
                if min_heap:
                    is_valid[hq.heappop(min_heap)[1]] = False

        else:
            hq.heappush(min_heap, (int(num), idx))
            hq.heappush(max_heap, (-int(num), idx))
            is_valid.append(True) #숫자가 크기 때문에 값으로 하는 것이 아니라 idx를 활용하여 valid처리함.
            idx += 1

    remove_invalid_data(max_heap)
    remove_invalid_data(min_heap)

    if max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")