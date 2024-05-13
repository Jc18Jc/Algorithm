N, K = map(int, input().split())
A = list(map(int, input().split()))
belt = [False for _ in range(N)]
b = answer = 0
while b < K:
    answer+=1
    if belt[-(answer%N)]:
        belt[-(answer%N)]=False
    for i in range(N-2, -1, -1):
        if belt[i-(answer%N)] and not belt[i-(answer%N)+1] and A[i-(answer%(2*N))+1]:
            A[i-(answer%(2*N))+1]-=1
            if not A[i-(answer%(2*N))+1]:
                b+=1
            belt[i-(answer%N)+1]=True
            belt[i-(answer%N)]=False
    if A[-(answer%(2*N))]:
        A[-(answer%(2*N))]-=1
        belt[-(answer%N)]=True
        if not A[-(answer%(2*N))]:
            b+=1

print(answer)