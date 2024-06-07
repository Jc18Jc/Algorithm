import sys

N, H = map(int, input().split())
top = [0 for _ in range(H+1)]
bottom = [0 for _ in range(H+1)]
answer = [0 for _ in range(H)]
for i in range(N):
  h=int(sys.stdin.readline())
  if i%2:
    top[H-h]+=1
  else:
    bottom[h]+=1

tmp = 0
for h in range(H, 0, -1):
  answer[h-1] = tmp + bottom[h]
  tmp+=bottom[h]
tmp=0
for h in range(0, H):
  answer[h] += tmp + top[h]
  tmp+=top[h]


print(min(answer), answer.count(min(answer)))
