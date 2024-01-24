import sys
ssr = sys.stdin.readline

n = int(ssr())
e = [[] for _ in range(n+1)]
leaf = []

for _ in range(n):
    tmp = list(map(int, ssr().split()))
    i=tmp[0]
    j=1
    while tmp[j]!=-1:
        e[i].append((tmp[j], tmp[j+1]))
        j+=2

def dfs(pre, cur, cost):
    if pre!=0 and len(e[cur])==1:
        return (cost, cur)
    c = (0, 0)
    for item in e[cur]:
        if item[0]==pre:
            continue
        tmp = dfs(cur, item[0], cost+item[1])
        if c[0] < tmp[0]:
            c=tmp
    return c

x = dfs(0, 1, 0)[1]
print(dfs(0, x, 0)[0])

