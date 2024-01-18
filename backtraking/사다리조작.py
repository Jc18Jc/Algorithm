import sys
ssr = sys.stdin.readline

n, m, h = map(int, ssr().split())
ladder = [[False for _ in range(h)]for _ in range(n)]
for _ in range(m):
    a, b = map(int, ssr().split())
    ladder[b-1][a-1]=True
    
def check():
    for i in range(n):
        location = i
        for j in range(h):
            if ladder[location][j]:
                location+=1
            elif location > 0 and ladder[location-1][j]:
                location-=1
        if location!=i:
            return False
    return True

maxRecur=4
def dfs(count, curi, curj):
    global maxRecur
    if maxRecur<=count:
        return
    if check():
        maxRecur=count
        return
    if maxRecur <= count+1:
        return
    for i in range(curi, n-1):
        if i==curi:
            j = curj
        else:
            j = 0
        while j < h:
            if not ladder[i][j]:
                if i==0 or i>0 and not ladder[i-1][j]:
                    ladder[i][j]=True
                    dfs(count+1, i, j+1)
                    ladder[i][j]=False
            j+=1

dfs(0, 0, 0)    
if maxRecur==4:
    print(-1)
else:
    print(maxRecur)


