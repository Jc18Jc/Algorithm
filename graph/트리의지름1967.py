import sys
ssr = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(ssr())
e = [[] for _ in range(n+1)]
leaf = []

for _ in range(n-1):
    a, b, c = map(int, ssr().split())
    e[a].append((b, c))
    e[b].append((a,c))

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

