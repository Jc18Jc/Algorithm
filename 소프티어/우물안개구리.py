import sys
input = sys.stdin.readline

N, M = map(int, input().split())
weight = list(map(int, input().split()))
conn = [[] for _ in range(N)]
for _ in range(M):
  A, B = map(int, input().split())
  conn[A-1].append(B-1)
  conn[B-1].append(A-1)
isStrong = [True for _ in range(N)]

for i in range(N):
  if not isStrong[i]:
    continue
  for target in conn[i]:
    if weight[target] >= weight[i]:
      isStrong[i] = False
      break
    else:
      isStrong[target] = False

print(isStrong.count(True))