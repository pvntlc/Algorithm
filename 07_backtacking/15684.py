import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def check_ladder():
    for i in range(n):
        garo = i
        for j in range(h):
            if board[j][garo]:
                garo += 1
            elif garo > 0 and board[j][garo-1]:
                garo -= 1

        if garo != i: return False

    return True


def ladder(count, x, y):
    global answer

    if check_ladder():
        answer = min(answer, count)

    elif count == 3 or answer <= count:
        return

    for i in range(x, h):
        if i == x:
            k = y
        else:
            k = 0

        for j in range(k, n-1):

            if not board[i][j] and not board[i][j+1]:
                if j >0 and board[i][j-1]:
                    continue

                board[i][j] = True
                ladder(count + 1, i, j+2)
                board[i][j] = False


n,m,h = map(int, input().split())
board = [[False] * n for _ in range(h)]
if m == 0:
    print(0)
else:

    for _ in range(m):
        a,b = map(int, input().split())
        board[a-1][b-1] = True

    answer = 4
    ladder(0,0,0)
    print(answer if answer < 4 else -1)



