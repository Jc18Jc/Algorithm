N,M,T = map(int, input().split())
array = list(list(map(int, input().split())) for _ in range(N))
turn = list(list(map(int, input().split())) for _ in range(T))

for x, d, k in turn:
    tmp = 1
    y=x-1
    while y < N:
        if d==0:
            array[y] = array[y][M-k:]+array[y][:M-k]
        else:
            array[y] = array[y][k:]+array[y][:k]
        flag=False
        tmp+=1
        y=x*tmp-1
    s=0
    count=0
    tt=[]
    for i in range(N):
        for j in range(M):
            if array[i][j] == 0:
                continue
            s+=array[i][j]
            count+=1
            if array[i][j]==array[i][j-1]:
                tt.append((i,j))
                tt.append((i,j-1))
            if array[i][j]==array[i][(j+1)%M]:
                tt.append((i,j))
                tt.append((i,(j+1)%M))
            if i != N-1 and array[i][j]==array[i+1][j]:
                tt.append((i, j))
                tt.append((i+1, j))
    if tt:
        for i, j in tt:
            array[i][j]=0
    else:
        if count==0: break
        if s%count==0:
            e=s//count
        else:
            e=s/count
        for i in range(N):
            for j in range(M):
                if array[i][j]==0 or array[i][j]==e:
                    continue
                if array[i][j] > e:
                    array[i][j]-=1
                else:
                    array[i][j]+=1
answer=0
for i in range(N):
    answer+=sum(array[i])
print(answer)