from heapq import heappop, heappush
N = int(input())
h=[]
D=int(input())
for _ in range(N-1):
  v = int(input())
  heappush(h, -v)
answer=0
while h and True:
  v = heappop(h)
  if -v < D:
    break
  D+=1
  answer+=1
  heappush(h, v+1)

print(answer)