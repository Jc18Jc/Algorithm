import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())

h = []
l = list(map(int, input().split()))
for j in range(N):
  heappush(h, l[j])
for i in range(N-1):
  l = list(map(int, input().split()))
  for j in range(N):
    heappush(h, l[j])
  for j in range(N):
    heappop(h)
    
print(heappop(h))