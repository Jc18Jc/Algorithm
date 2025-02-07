import sys
input = sys.stdin.readline

N, K = map(int, input().split())

tree = [0] * (4 * N)

def init(start, end, v):
  if start==end:
    tree[v]=array[start]
  else:
    mid = (start+end)//2

    left = init(start, mid, v*2)
    right = init(mid+1, end, v*2+1)
    
    tree[v]=left+right
  return tree[v]

def find(start, end, sindex, eindex, v):
  if sindex > end or eindex < start:
    return 0
  if sindex <= start and eindex >= end:
    return tree[v]
  
  mid = (start+end)//2

  left = find(start, mid, sindex, eindex, v*2)
  right = find(mid+1, end, sindex, eindex, v*2+1)

  return left+right

array = list(map(int, input().split()))

init(0, N-1, 1)

for _ in range(K):
  sindex, eindex = map(int ,input().split())
  result = find(0, N-1, sindex-1, eindex-1, 1)
  print("{0:.2f}".format(result/float(eindex-sindex+1)))

