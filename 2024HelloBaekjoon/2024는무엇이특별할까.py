import sys
ssr = sys.stdin.readline

t = int(ssr())

for _ in range(t):
    n, k = map(int, ssr().split())
    tmp=1
    for _ in range(k):
        tmp = tmp<<1
        if tmp > n:
            print(0)
            break
    if tmp > n:
        continue
    n=n-tmp
    print((n//(1<<(k+1)))+1)