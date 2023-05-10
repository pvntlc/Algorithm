# 2812번 : 크게 만들기 – Gold 3
import sys
import heapq as hq

input = sys.stdin.readline
INF = sys.maxsize
'''
- 앞에 있는 숫자가 뒤에 있는 숫자보다 작으면 지우는 방식으로 진행됨.
- 어차피 남는 수는 n-k자리 수!
- 가능한 앞자리에 큰 수를 배치하는 것이 유리하다.
- 수의 앞자리부터 탐색하며, 스택에 차례대로 저장
- 직전 자리보다 큰 수가 나오면 스택의 top이 자신보다 크거나 같아질 때까지 pop한 뒤에 추가

 ex) 1924 에서 2개를 지워서 큰 수를 만들어야 한다면
    stack: []           이번 숫자 '1' -> stack: ['1']
    stack: ['1']        이번 숫자 '9' -> stack: ['9']
    stack: ['9']        이번 숫자 '2' -> stack: ['9', '2']
    stack: ['9', '2']   이번 숫자 '4' -> stack: ['9', '4']

    답: 94

- 정확히 k개의 수를 지워야 함을 유의
'''

n, K = map(int, input().split())
line = list(input().rstrip())
answer = []
k = 0

for num in line:
    while answer and answer[-1] < num and k < K:
        answer.pop()
        k += 1
    answer.append(num)

print(''.join(answer))