import sys
input = sys.stdin.readline

n_list = []
idx = 1
sum_idx = 0
while True:
    if sum_idx <= 2147483648:
        sum_idx += idx
        n_list.append(sum_idx)
        sum_idx += idx
        n_list.append(sum_idx)
        idx += 1
    else:
        break

for _ in range(int(input())):
    x,y = map(int, input().split())

    for i in range(len(n_list)):
        if n_list[i] >= (y-x):
            print(i+1)
            break