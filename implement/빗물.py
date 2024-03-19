H, W = map(int, input().split())
hei = list(map(int, input().split()))

save = [0 for _ in range(H+1)]
answer = 0
maxh = 0
for i in range(W):
    h = hei[i]
    for j in range(1, h+1):
        answer+=save[j]
        save[j]=0
    for j in range(h+1, maxh+1):
        save[j]+=1
    maxh = maxh if maxh > h else h

print(answer)
    
### 코드리뷰 ###
'''
import sys
ssr = sys.stdin.readline()

h, w = map(int, ssr.split())
wall = list(map(int, sys.stdin.readline().split()))

ans = 0
for i in range(1, w - 1):
    left_max = max(wall[:i])
    right_max = max(wall[i + 1 :])
    secondWall = min(left_max, right_max)
    if wall[i] < secondWall: # 좌우로 자기보다 큰 벽이 있으면 더해줬구나 내것보다 훨씬 효율적이네
        ans += secondWall - wall[i]
print(ans)

'''