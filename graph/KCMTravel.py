import sys
input = sys.stdin.readline
from collections import deque

def dijkstra(N,M,E):
    costList = [[10**6 for _ in range(N+1)] for _ in range(M+1)]
    pq=deque()
    pq.append((0,0,1))
    while pq:
        distance, cost, node=pq.popleft()
        if costList[cost][node] >= distance:
            for v,c,d in E[node]:
                if cost+c <= M and costList[cost+c][v] > distance+d:
                    pq.append((distance+d,cost+c,v))
                    for j in range(cost+c, M+1):
                        if costList[j][v] > distance+d:
                            costList[j][v]=distance+d
                        else:
                            break
    return 'Poor KCM' if costList[M][N]==10**6 else costList[M][N]

def main():
    input()
    N, M, K = map(int, input().split())
    E = [[] for _ in range(N+1)]
    for _ in range(K):
        u,v,c,d=map(int, input().split())
        E[u].append((v,c,d))
    for i in range(1,N+1):
        E[i].sort(key=lambda x:x[2])
    print(dijkstra(N,M,E))

main()


### 코드리뷰 ###
'''
import sys
input=sys.stdin.readline
T=int(input());INF=1<<30
N,M,K=map(int,input().split())
dist=[[INF]*(M+2) for i in range(N)];dist[0][0]=0;
edge=[[] for i in range(N)]
for _ in range(K):
  u,v,c,d=map(int,input().split())
  edge[u-1].append((v-1,c,d))
# 다익스트라 개념이 아니고, 각 코스트 별로 갈 수 있는 곳을 찍었네
# M*N*? 간선 개수는 시간 복잡도에 어떻게 들어가는지 모르겠다
for m in range(M+1):
  for u in range(N):
    if dist[u][m]>=dist[u][-1]:continue
    di=dist[u][-1]=dist[u][m] # 마지막(M+1)칸에는 가장 작은 dist 넣어줌
    for v,c,d in edge[u]:
      if c+m<=M:dist[v][c+m]=min(di+d,dist[v][c+m])
if (res:=dist[N-1][-1])==INF:print("Poor KCM")
else:print(res)
'''