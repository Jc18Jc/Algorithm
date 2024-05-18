N=int(input())

def dfs(start,s):
    e=array[s]
    if visited[e]:
        return False
    visited[e]=True
    if e==start:
        answer.append(s)
        return True
    if dfs(start, array[s]):
        answer.append(s)
        return True
    return False

array=[0]+[int(input()) for _ in range(N)]
answer=[]
for i in range(1,N+1):
    visited=[False for _ in range(N+1)]
    dfs(i,array[i])
answer=list(set(answer))
print(len(answer))
answer.sort()
for i in answer:
    print(i)