import sys
import math
import heapq

n = int(sys.stdin.readline())

starLoc = [[0, 0]]

for _ in range(1, n + 1):
    x, y = map(float, sys.stdin.readline().split())

    starLoc.append([x, y])

graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
heap = [[0, 1]]

for s in range(1, n + 1):
    for e in range(s + 1, n + 1):
        dist = math.sqrt(
            (starLoc[s][0] - starLoc[e][0]) ** 2 + (starLoc[s][1] - starLoc[e][1]) ** 2
        )
        graph[s].append([dist, e])
        graph[e].append([dist, s])

totalWeight = 0
count = 0
while heap:
    w, s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = True
        totalWeight += w
        for v in graph[s]:
            heapq.heappush(heap, v)

print("{:.2f}".format(totalWeight))