# 브론즈
N, M = map(int, input().split())
array=list(map(int, input().split()))

answer=0
for i in range(N-2):
    a = array[i]
    for j in range(i+1, N-1):
        b = array[j]
        for k in range(j+1, N):
            c = array[k]
            if a+b+c <= M:
                answer = answer if a+b+c < answer else a+b+c
print(answer)