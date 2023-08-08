import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n,s = map(int, input().split())
numbers = list(map(int, input().split()))
answers = []
count = 0

def num_sum(start):
    global count
    if sum(answers) == s and len(answers) > 0:
        count += 1

    for i in range(start, n):
        answers.append(numbers[i])
        num_sum(i+1)
        answers.pop()

num_sum(0)
print(count)