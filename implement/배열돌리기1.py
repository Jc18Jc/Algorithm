N,M,R = map(int, input().split())

for i in range(min(N,M)//2):
    r=R%((N-i*2)*2+(M-i*2)*2-4)
