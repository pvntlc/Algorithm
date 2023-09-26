import sys
input = sys.stdin.readline
INF = sys.maxsize
'''
    https://www.acmicpc.net/problem/1050
'''
n,m = map(int, input().split())
n_dict = dict()
n_list = []
for _ in range(n):
    text, value = input().rstrip().split()
    n_dict[text] = value

rest_arr = []
def solve():
    global answer
    for _ in range(m):
        a, b= input().rstrip().split('=')
        temp = []
        temp.append(b.split('+'))
        for t in temp:
            sum_num = 0
            number = 0
            flag = True
            for text in t:
                for i in range(len(text)):
                    if text[i].isdigit():
                        continue
                    else:
                        number = text[:i]
                        break
                if text[i:] in n_dict.keys():
                    sum_num += int(number) * int(n_dict[text[i:]])

                else:
                    flag = False
            if flag:
                if a in n_dict.keys():
                    n_dict[a] = min(sum_num, int(n_dict[a]))
                else:
                    n_dict[a] = sum_num
                rest_arr.append([a, b])
            else:
                rest_arr.append([a, b])

    for _ in range(m):
        for a, b in rest_arr:
            temp = []
            temp.append(b.split('+'))
            for t in temp:
                sum_num = 0
                number = 0
                flag = True
                for text in t:

                    for i in range(len(text)):
                        if text[i].isdigit():
                            continue
                        else:
                            number = text[:i]
                            break
                    if text[i:] in n_dict.keys():
                        sum_num += int(number) * int(n_dict[text[i:]])
                    else:
                        flag = False

                if flag:
                    if a in n_dict.keys():
                        n_dict[a] = min(sum_num, int(n_dict[a]))
                    else:
                        n_dict[a] = sum_num

solve()
if 'LOVE' in n_dict.keys():
    if int(n_dict['LOVE']) > 1000000000:
        print(1000000001)
    else:
        print(n_dict['LOVE'])
else:
    print(-1)