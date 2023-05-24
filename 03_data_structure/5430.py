# 5430번 : AC - Gold 5
import sys
input = sys.stdin.readline
"""

"""
def solution():
    for _ in range(int(input())): #테스트 케이스 개수
        commands = [*map(len, input().rstrip().replace("RR", "").split("R"))]
        is_reversed = (len(commands) + 1) % 2
        n = int(input())
        n_list = input().strip("[]\n").split(",")

        front = sum(commands[0::2])
        back = sum(commands[1::2])

        if front + back > n:
            print("error")
            continue
        else:
            n_list = n_list[front:n-back]

        if is_reversed:
            n_list.reverse()
        print("[" , ",".join(n_list), "]", sep="")
solution()