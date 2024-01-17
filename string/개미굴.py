import sys
ssr=sys.stdin.readline

n=int(ssr())

d=dict()

def dfs(tmpd, count):
    if len(tmpd)==0:
        return
    dkey = list(tmpd.keys())
    dkey.sort()
    for i in range(len(dkey)):
        for _ in range(count):
            print('--', end='')
        print(dkey[i])
        dfs(tmpd[dkey[i]], count+1)

for _ in range(n):
    l = list(ssr().strip().split())
    tmpd = d
    for i in range(int(l[0])):
        if l[i+1] in tmpd:
            tmpd=tmpd[l[i+1]]
        else:
            tmpd[l[i+1]]=dict()
            tmpd=tmpd[l[i+1]]

dfs(d, 0)