a=int(input())
b = list(map(int,input().split()))
ori = b
s=list(map(int,input().split()))
c = [0,1,2] * (a // 3)
new = [0] * a
cnt = 0

while b!= c:
    for i in range(a):
        new[s[i]] = b[i]

    b = new
    new = [0] * a
    cnt += 1
    if ori == b:
        cnt =- 1
        break
print(cnt)