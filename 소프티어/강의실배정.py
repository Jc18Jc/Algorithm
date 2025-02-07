import sys
input = sys.stdin.readline

N = int(input())

array = [list(map(int, input().split())) for _ in range(N)]

array.sort(key = lambda x:x[1])

answer = 1
start = array[N-1][0]
end = array[N-1][1]

for i in range(N-2, -1, -1):
  nstart, nend = array[i]
  if nend > start and nstart > start:
    start, end = nstart, nend
    continue
  if nend <= start:
    answer+=1
    start, end = nstart, nend

print(answer)