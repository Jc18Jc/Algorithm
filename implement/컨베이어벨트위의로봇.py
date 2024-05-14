N, K = map(int, input().split())
A = list(map(int, input().split()))
belt = [False for _ in range(N)]
b, answer = 0, 0
while b < K:
    answer+=1
    for i in range(N-2, -1, -1):
        if belt[i]:
            belt[i+1]=True
            belt[i]=False
    if belt[-1]:
        belt[-1]=False
    d=-(answer%(2*N))
    for i in range(N-2, -1, -1):
        if belt[i] and not belt[i+1] and A[i+1+d]:
            A[i+1+d]-=1
            if not A[i+1+d]:
                b+=1
            belt[i+1]=True
            belt[i]=False
    if belt[-1]:
        belt[-1]=False
    if A[d] and not belt[0]:
        A[d]-=1
        belt[0]=True
        if not A[d]:
            b+=1

print(answer)