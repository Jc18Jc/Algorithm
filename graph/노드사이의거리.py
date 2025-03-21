import sys
input = sys.stdin.readline

N, M = map(int, input().split())

edges = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

def dfs(node, e, value):
  global visited
  answer = 10**8
  if node == e:
    return value

  for next, v in edges[node]:
    if not visited[next]:
      visited[next]=True
      result = dfs(next, e, value+v)
      answer = result if answer > result else answer
      visited[next]=False
  
  return answer

for _ in range(N-1):
  a, b, v = map(int, input().split())
  edges[a].append((b, v))
  edges[b].append((a, v))

searchList = []

for _ in range(M):
  s, e = map(int, input().split())
  searchList.append((s, e))

for s, e in searchList:
  visited[s] = True
  print(dfs(s, e, 0))
  visited[s] = False
  