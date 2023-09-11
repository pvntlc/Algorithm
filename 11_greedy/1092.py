import sys
input = sys.stdin.readline

'''

'''

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort(reverse=True)
m = int(input())
m_list = list(map(int, input().split()))
m_list.sort(reverse=True)
time = 0
def solve():
    global time
    if n_list[0] < m_list[0]:
        print(-1)
        return
    while len(m_list) > 0:
        for cranes in n_list:
            for boxes in m_list:
                if cranes >= boxes:
                    m_list.remove(boxes)
                    break
        time += 1
    print(time)
    return

solve()
