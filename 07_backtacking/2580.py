import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

graph = [list(map(int, input().split())) for _ in range(9)]
zero_list = []

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            zero_list.append((i,j))

def check_row(row, number):
    for i in range(9):
        if number == graph[row][i]:
            return False
    return True

def check_col(col, number):
    for i in range(9):
        if number == graph[i][col]:
            return False
    return True

def check_nemo(row, col, number):
    nrow = row // 3 * 3
    ncol = col // 3 * 3
    for i in range(3):
        for j in range(3):
            if number == graph[nrow+i][ncol+j]:
                return False
    return True

def sdoku(count):
    if count == len(zero_list):
        for i in range(9):
            print(' '.join(map(str,graph[i])))
        exit(0)

    for i in range(1,10):
        r = zero_list[count][0]
        c = zero_list[count][1]

        if check_nemo(r,c,i) and check_col(c, i) and check_row(r,i):
            graph[r][c] = i
            sdoku(count + 1)
            graph[r][c] = 0

sdoku(0)