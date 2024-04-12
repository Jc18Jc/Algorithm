N,M,K = map(int,input().split())
board=[[[0, 0, 'N'] for _ in range(N)]for _ in range(N)]
delta = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def checkDir(original, next):
    td = original
    if original=='N':
        td=next
    elif original=='E':
        if next%2==1: td='F'
    elif original=='O':
        if next%2==0: td='F'
    elif original=='F':
        td='F'
    else:
        if original%2==0 and next%2==0: td='E'
        elif original%2==1 and next%2==1: td='O'
        else: td='F'
    return td

def order():
    tmpBoard=[[[0, 0, 'N']for _ in range(N)]for _ in range(N)]
    count=[[0 for _ in range(N)]for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j][0]>0:
                m,s,dir=board[i][j]
                p=2
                if dir=='E' or dir=='O' or dir=='F':
                    d=0
                    m=m//5
                    if m==0: continue
                    if dir=='F': d=1
                else:
                    d, p = dir, 8
                while d<8:
                    di, dj = i+delta[d][0]*s, j+delta[d][1]*s
                    while di < 0: di+=N
                    while dj < 0: dj+=N
                    di%=N
                    dj%=N
                    tmpBoard[di][dj][0]+=m
                    tmpBoard[di][dj][1]+=board[i][j][1]
                    tmpBoard[di][dj][2]=checkDir(tmpBoard[di][dj][2], d)
                    count[di][dj]+=1
                    d+=p
    for i in range(N):
        for j in range(N):
            if count[i][j]>1:
                tmpBoard[i][j][1]=tmpBoard[i][j][1]//count[i][j]
    return tmpBoard

for _ in range(M):
    r,c,m,s,d=map(int,input().split())
    board[r-1][c-1]=[m,s,d]
for _ in range(K):
    board=order()
answer=0
for i in range(N):
    for j in range(N):
        d=board[i][j][2]
        if d=='O' or d=='F' or d=='E': answer+=(board[i][j][0]//5)*4
        else: answer+=board[i][j][0]
print(answer)

### 코드리뷰 ###
'''
N, M, K = map(int, input().split())
fireballs = []
for _ in range(M):
    _r, _c, _m, _s, _d = list(map(int, input().split()))
    fireballs.append([_r-1, _c-1, _m, _s, _d])

MAP = [[[] for _ in range(N)] for _ in range(N)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    while fireballs: # 처음에 내가 생각한게 이런거였는데 구현을 못했다.. 훨씬 깔끔
        cr, cc, cm, cs, cd = fireballs.pop(0) # 이렇게 할거면 데크하던가 아니면 그냥 pop으로 끝에서 꺼내써도 될 듯
        nr = (cr + cs * dx[cd]) % N # 음수여도 괜찮나 ?? 와 상관없네  -1 % 8 = 7
        nc = (cc + cs * dy[cd]) % N
        MAP[nr][nc].append([cm, cs, cd])
    for r in range(N):
        for c in range(N):
            if len(MAP[r][c]) > 1:
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(MAP[r][c])
                while MAP[r][c]:
                    _m, _s, _d = MAP[r][c].pop(0) # 여기도 데크나 그냥 pop
                    sum_m += _m
                    sum_s += _s
                    if _d % 2:
                        cnt_odd += 1
                    else:
                        cnt_even += 1
                if cnt_odd == cnt or cnt_even == cnt:
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                if sum_m//5:
                    for d in nd:
                        fireballs.append([r, c, sum_m//5, sum_s//cnt, d])
            if len(MAP[r][c]) == 1:
                fireballs.append([r, c] + MAP[r][c].pop())

print(sum([f[2] for f in fireballs]))
'''