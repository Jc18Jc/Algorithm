import sys
ssr = sys.stdin.readline

n, k = map(int, ssr().split())

if k < 5:
    exit(print(0))

setList = []
count=0

d = set(['a','n','c','i','t'])
uniqueSet = set()
for _ in range(n):
    s = ssr().strip()
    s = set(s)
    s=s-d
    if len(s)==0:
        count+=1
        continue
    uniqueSet = uniqueSet|s
    setList.append(s)

k-=5
if len(uniqueSet) <= k:
    exit(print(n))

n=len(setList)
uniqueList = list(uniqueSet)
def dfs(m, deleteList, index):
    if m == k:
        deleteSet = set(deleteList)
        lc = 0
        for i in range(n):
            if not setList[i]-deleteSet:
                lc+=1
        return lc

    mc = 0
    for i in range(index+1, len(uniqueList)):
        result = dfs(m+1, deleteList+[uniqueList[i]], i)
        mc = mc if mc > result else result
    return mc
print(dfs(0, [], -1)+count)
