from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
edges = [[] for _ in range(N+1)]

while True:
  a, b = map(int, input().split())
  if (a == -1):
    break
  edges[a].append(b)
  edges[b].append(a)

minScore = 10**8
candList = []

for i in range(1, N+1):
  visited = [False for _ in range(N+1)]
  visited[i] = True
  d = deque()
  d.append((i, 0))
  score=0

  while d:
    node, distance = d.popleft()
    score = distance if score < distance else score
    for next in edges[node]:
      if not visited[next]:
        d.append((next, distance+1))
        visited[next]=True
  if score < minScore:
    minScore = score
    candList.clear()
    candList.append(i)
  elif score == minScore:
    candList.append(i)

print(minScore, len(candList))
print(*candList)