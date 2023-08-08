import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
numbers = list(map(int, input().split()))
answer = []
count = 0
max_value = 0

def max_sum():
    global count, max_value

    if len(answer) == n:
        answer_sum = 0
        for i in range(n-1):
            answer_sum += abs(numbers[answer[i+1]] - numbers[answer[i]])
        max_value = max(max_value, answer_sum)
        return

    for i in range(n):
        if not i in answer:
            answer.append(i)
            max_sum()
            answer.pop()

max_sum()
print(max_value)