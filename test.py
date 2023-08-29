import sys

input = sys.stdin.readline
answer_list = []
for i in range(45):
    list11 = list(input().rstrip().split(","))
    answer_list.append(list11)

for i in range(45):
    if i == 0 or i == 44 or i == 43:
        print(*answer_list[i], end="")
    else:
        print(*answer_list[i], end=",")