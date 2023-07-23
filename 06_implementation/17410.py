# 17140번 : 이차원 배열과 연산 - Gold 4
import sys
input = sys.stdin.readline
INF = sys.maxsize
'''
https://www.acmicpc.net/problem/17140

1. 크기가 3x3인 배열 A가 있다.
2. R연산 수행 ( 행의 개수 >= 열의 개수 )
3. C연산 수행 ( 행의 개수 < 열의 개수 )
'''
def r_cal(matrix):
    new_matrix = []
    for i in matrix:
        n_dict = dict()

        for k in i:
            if k not in n_dict.keys() and k != 0:
                n_dict[k] = 1
            elif k in n_dict.keys():
                n_dict[k] += 1

        result_list = []

        for num in n_dict.keys():
            result_list.append((num, n_dict[num]))

        result_list.sort(key = lambda x : (x[1], x[0]))

        temp = []
        for x,y in result_list:
            temp.append(x)
            temp.append(y)

        new_matrix.append(temp)

    max_value = 0
    for i in range(len(new_matrix)):
        max_value = max(max_value, len(new_matrix[i]))

    for i in range(len(new_matrix)):
        value = max_value - len(new_matrix[i])
        for k in range(value):
            new_matrix[i].append(0)

    return new_matrix


def c_cal(matrix):
    matrix = list(zip(*matrix))
    new_matrix = []
    for i in matrix:
        n_dict = dict()

        for k in i:
            if k not in n_dict.keys() and k != 0:
                n_dict[k] = 1
            elif k in n_dict.keys():
                n_dict[k] += 1

        result_list = []

        for num in n_dict.keys():
            result_list.append((num, n_dict[num]))

        result_list.sort(key=lambda x: (x[1], x[0]))

        temp = []
        for x, y in result_list:
            temp.append(x)
            temp.append(y)

        new_matrix.append(temp)

    max_value = 0
    for i in range(len(new_matrix)):
        max_value = max(max_value, len(new_matrix[i]))

    for i in range(len(new_matrix)):
        value = max_value - len(new_matrix[i])
        for k in range(value):
            new_matrix[i].append(0)

    new_matrix = list(zip(*new_matrix))
    return new_matrix

r,c,k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(3)]
result = 0

for _ in range(101):
    if len(matrix) >= r and len(matrix[0]) >= c:
        if matrix[r-1][c-1] == k:
            print(result)
            break

    if len(matrix) >= len(matrix[0]):
        matrix = r_cal(matrix)
        result += 1
    else:
        matrix = c_cal(matrix)
        result += 1
else:
    print(-1)
