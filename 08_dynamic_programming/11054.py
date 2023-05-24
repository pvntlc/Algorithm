# 11054번 : 가장 긴 바이토닉 부분 수열 - Gold 4
import sys
input = sys.stdin.readline
INF = sys.maxsize
'''
증가하는 수열 중에 가장 긴 수열 + 감소하는 수열 중 가장 긴 수열이 가장 큰 값이 정답!

10
주어지는 수열 : 1 5 2 1 4 3 4 5 2 1
증가하는 수열 : 1 2 2 1 3 3 4 5 2 1
감소하는 수열 : 1 5 2 1 4 3 3 3 2 1

인덱스가 7인 값이 가장 큰 수 일 때 바이토닉 수열이 가장 길기 때문에,
증가수열 [1,2,3,4,5] + 감소수열 [5,2,1] - 중복부분[5] = [1,2,3,4,5,2,1]이 된다.
'''

n = int(input())
n_list = list(map(int, input().split()))
reverse_n_list = n_list[::-1]

increase = [1 for i in range(n)]
decrease = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if n_list[i] > n_list[j]:
            increase[i] = max(increase[i], increase[j] + 1)
        if reverse_n_list[i] > reverse_n_list[j] :
            decrease[i] = max(decrease[i], decrease[j] + 1)
max_value = 0
for i in range(n):
    x,y = increase[i], decrease[n-i-1]
    max_value = max(max_value, x+y)
print(max_value-1)