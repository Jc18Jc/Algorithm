import sys
ssr = sys.stdin.readline

n, m = map(int, ssr().split())

home = []
chi = []

for i in range(n):
    l = list(map(int, ssr().split()))
    for j in range(n):
        if l[j]==1:
            home.append((i, j))
        elif l[j]==2:
            chi.append((i, j))

hl = len(home)
cl = len(chi)

def dfs(count, l, index):
    if count == m:
        total = 0
        for i in range(hl):
            value = 501
            for j in range(m):
                tmp=abs(chi[l[j]][1]-home[i][1])+abs(chi[l[j]][0]-home[i][0])
                value = value if value < tmp else tmp
            total+=value
        return total
    if index >= cl:
        return 501*100
    total = 501*100
    for i in range(index+1, cl):
        result = dfs(count+1, l+[i], i)
        total = total if total < result else result
    return total

print(dfs(0, [], -1))