import sys
input = sys.stdin.readline

h,m,s = list(map(int, input().split()))
num = int(input())
time = h*3600 + m*60 + s


def change_time(c):
    global time
    time = (time + c) % 86400



def print_time(time):
    h = time // 3600
    m = (time-3600*h)//60
    s = (time-3600*h - 60*m)
    print(h,m,s)

for i in range(num):
    n_list = list(map(int, input().split()))
    if(n_list[0] == 1):
        change_time(n_list[1])
    elif(n_list[0] == 2):
        change_time(-n_list[1])
    else:
        print_time(time)