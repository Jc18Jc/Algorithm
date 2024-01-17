import sys
ssr = sys.stdin.readline

n, m =map(int, ssr().split())

b = []

for _ in range(n):
    b.append(list(map(int, ssr().split())))
tmp=[]
for i in range(n):
    for j in range(m):
        if i+3 < n:
            tmp.append(b[i][j]+b[i+1][j]+b[i+2][j]+b[i+3][j])
        if j+3 < m:
            tmp.append(b[i][j]+b[i][j+1]+b[i][j+2]+b[i][j+3])
        if i+1 < n and j+1 < m:
            tmp.append(b[i][j]+b[i][j+1]+b[i+1][j]+b[i+1][j+1])
        if i+2 < n and j+1 < m:
            tmp.append(b[i][j]+b[i+1][j]+b[i+2][j]+b[i+2][j+1])
        if i-1 > -1 and j+2 < m:
            tmp.append(b[i][j]+b[i][j+1]+b[i][j+2]+b[i-1][j+2])
        if i-2 > -1 and j -1 > -1:
            tmp.append(b[i][j]+b[i-1][j]+b[i-2][j]+b[i-2][j-1])
        if i+1 < n and j-2 > -1:
            tmp.append(b[i][j]+b[i][j-1]+b[i][j-2]+b[i+1][j-2])
        if i+2 < n and j-1 > -1:
            tmp.append(b[i][j]+b[i+1][j]+b[i+2][j]+b[i+2][j-1])
        if i+1 < n and j+2 < m:
            tmp.append(b[i][j]+b[i][j+1]+b[i][j+2]+b[i+1][j+2])
        if i-2 > -1 and j+1 < m:
            tmp.append(b[i][j]+b[i-1][j]+b[i-2][j]+b[i-2][j+1])
        if i-1 > -1 and j-2 > -1:
            tmp.append(b[i][j]+b[i][j-1]+b[i][j-2]+b[i-1][j-2])
        if i+2 < n and j+1 < m:
            tmp.append(b[i][j]+b[i+1][j]+b[i+1][j+1]+b[i+2][j+1])
        if i-1 > -1 and j+2 < m:
            tmp.append(b[i][j]+b[i][j+1]+b[i-1][j+1]+b[i-1][j+2])
        if i+2 < n and j-1 > -1:
            tmp.append(b[i][j]+b[i+1][j]+b[i+1][j-1]+b[i+2][j-1])
        if i+1 < n and j+2 < m:
            tmp.append(b[i][j]+b[i][j+1]+b[i+1][j+1]+b[i+1][j+2])
        if i+1 < n and j+2 < m:
            tmp.append(b[i][j]+b[i][j+1]+b[i][j+2]+b[i+1][j+1])
        if i-2 > -1 and j+1 < m:
            tmp.append(b[i][j]+b[i-1][j]+b[i-2][j]+b[i-1][j+1])
        if i-1 > -1 and j+2 < m:
            tmp.append(b[i][j]+b[i][j+1]+b[i][j+2]+b[i-1][j+1])
        if i-2 > -1 and j-1 > -1:
            tmp.append(b[i][j]+b[i-1][j]+b[i-2][j]+b[i-1][j-1])

print(max(tmp))