import sys
sys.setrecursionlimit(10**5)

def dfs(num, count, level):
    lc, rc = 0, 0
    if node[num][0] != -2:
        lc = dfs(node[num][0], count, level+1)
    count+=lc
    mnm[level][0] = mnm[level][0] if count > mnm[level][0] else count
    mnm[level][1] = mnm[level][1] if count < mnm[level][1] else count
    if node[num][1] != -2:
        rc = dfs(node[num][1], count+1, level+1)
    return rc+lc+1

def fidnRoot():
    c = [False for _ in range(N)]
    for a, b in node:
        if a!=-2:
            c[a]=True
        if b!=-2:
            c[b]=True
    for i in range(N):
        if not c[i]:
            return i

N = int(input())
node = [None]*N
mnm = [[10000, -1] for _ in range(10000)]
for _ in range(N):
    a, b, c = map(int, input().split())
    node[a-1]=[b-1, c-1]
dfs(fidnRoot(), 0, 0)
m = 0
mi = 0
for i in range(10000):
    if mnm[i][1]-mnm[i][0] > m:
        m = mnm[i][1]-mnm[i][0]
        mi=i
print(mi+1, m+1)