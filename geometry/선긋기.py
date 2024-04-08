import sys
N=int(input())
array = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
array.sort()

answer=0
i=0
while i < N:
    j=i+1
    while j < N and array[i][1] >= array[j][1]:
        j+=1
    if j == N or array[i][1] < array[j][0]:
        answer+=array[i][1]-array[i][0]
    else:
        answer+=array[j][0]-array[i][0]
    i=j

print(answer)