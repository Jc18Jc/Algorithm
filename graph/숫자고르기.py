def dfs(v,i):
    visited[v]=True
    w=array[v]
    if not visited[w]:
        dfs(w,i)
    elif visited[w] and w==i:
        result.append(w)
N=int(input())
array=[0]+[int(input()) for _ in range(N)]
result=[]
for i in range(1,N+1):
    visited=[False]*(N+1)
    dfs(i,i)
print(len(result))
result.sort()
for i in result:
    print(i)