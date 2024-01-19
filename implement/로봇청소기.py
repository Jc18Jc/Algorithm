import sys
ssr = sys.stdin.readline

n, m = map(int, ssr().split())
loci, locj, d = map(int, ssr().split())
di = [0, -1, 0, 1]
dj = [-1, 0, 1, 0]
ri = [1, 0, -1, 0]
rj = [0, -1, 0, 1]
board = []

for _ in range(n):
    board.append(list(map(int, ssr().split())))

count=0
while True:
    if not board[loci][locj]:
        board[loci][locj]=2
        #print(loci, locj)
        count+=1
    flag=True
    for k in range(4):
        i = loci+di[(d+4-k)%4]
        j = locj+dj[(d+4-k)%4]
        if -1 < i < n and -1 < j < m and not board[i][j]:
            loci=i
            locj=j
            flag=False
            d=((d+4-k)%4+3)%4
            break
    if flag:
        i = loci+ri[d]
        j = locj+rj[d]
        if -1 < i < n and -1 < j < m and board[i][j]==2:
            loci=i
            locj=j
        else:
            break

print(count)