import sys
input = sys.stdin.readline

N, M = map(int, input().split())
points = list(list(map(int, input().split())) for _ in range(N))

def dis(p1, p2):
  return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(1/2)

def union(n1, n2, value):
  p1 = find(n1)
  p2 = find(n2)
  if p1 == p2:
    return 0
  if p1 > p2:
    parents[p1]=p2
  else:
    parents[p2]=p1
  return value

    
def find(n1):
  if parents[n1]!=n1:
    return find(parents[n1])
  return n1

w = []
for i in range(N):
  for j in range(i+1, N):
    w.append((dis(points[i], points[j]), i, j))
w.sort()

parents = [i for i in range(N)]
answer = 0

for _ in range(M):
  a, b = map(int, input().split())
  answer += union(a-1, b-1, 0)

for v, n1, n2 in w:
  answer += union(n1, n2, v)

print("{:.2f}".format(answer))