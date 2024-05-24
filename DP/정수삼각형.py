import sys
N=int(input())
array = [None for _ in range(N)]
for i in range(N):
    array[i]=list(map(int, input().split()))
answer = [[0 for _ in range(N)] for _ in range(N)]
answer[0][0]=array[0][0]
for i in range(1, N):
    for j in range(len(array[i])):
        if j==0:
            answer[i][j]=answer[i-1][0]
        elif j==len(array[i])-1:
            answer[i][j]=answer[i-1][i-1]
        else:
            answer[i][j]=max(answer[i-1][j-1], answer[i-1][j])
        answer[i][j]+=array[i][j]
print(max(answer[N-1]))