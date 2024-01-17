import sys
ssr = sys.stdin.readline

n=int(ssr())
num = ['#' for _ in range(2*n+1)]
tmp = list(map(int, ssr().split()))
for i in range(n):
    num[2*i+1]=tmp[i] 
n=n*2+1
r, p = -1, -1
res = [0 for _ in range(n)]

for i in range(1, n):
    if i > r:
        p, r = i, i
        while r < n and 2*p >= r and num[r] == num[2*p-r]: r+=1
        r-=1
        res[i]=r-i
    else:
        j=2*p-i
        if res[j] > r-i:
            res[i] = r-i
        elif res[j] == r-i:
            p= i
            while r < n and 2*p >= r and num[r] == num[2*p-r]: r+=1
            r-=1
            res[i]=r-i
        else:
            res[i]=res[j]

m = int(ssr())

for _ in range(m):
    a, b = map(int, ssr().split())
    p = a+b-1
    if res[p] >= b-a+1:
        print(1)
    else:
        print(0)