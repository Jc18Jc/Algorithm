import sys
ssr = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m = map(int, ssr().split())
friend = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, ssr().split())
    friend[a].append(b)
    friend[b].append(a)

visited = [True for _ in range(n)]

def dfs(i, count):
    if count > 3:
        exit(print(1)) 
    for item in friend[i]:
        if visited[item]:
            visited[item]=False
            dfs(item, count+1)
            visited[item]=True

for i in range(n):
    visited[i] = False
    dfs(i, 0)
    visited[i] = True

print(0)