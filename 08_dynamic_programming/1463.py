# 1463번 : 1로 만들기 - Silver 3
import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize
"""
아무 생각없이 반복문과 조건문을 걸어서 풀게 되면, 횟수의 최소값을 구할 수 없다.
예를 들어, 10이 있을 때 10 - 5 - 4 - 3 - 1의 방식으로 가기 때문이다.
따라서 DP를 활용해서 각 수에서의 최소값을 갱신하면서 가야 한다.

10을 넣었을 때, DP 배열은 다음과 같아진다.
인덱스    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 
배열값    | 0 | 0 | 1 | 1 | 2 | 3 | 2 | 3 | 3 | 2 |  3 |
그래서 정답은 3이 되는 것이다.
"""
n = int(input())
dp = [0,0,1,1] # 앞에는 무조건 0,0,1,1이므로.

for i in range(4,n+1):
    dp.append(dp[i-1] + 1)
    # 2로 나누어 떨어질 때
    if i % 2 == 0 :
        # 1을 뺄 때와 2로 나눌 때 더 작은 횟수인 것을 저장
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0 :
        # 앞에서 구한 arr[i]과 3으로 나눌 때 더 작은 횟수인 것을 저장
        dp[i] = min(dp[i], dp[i//3] + 1)
print(dp[n])