import sys
ssr = sys.stdin.readline

t=int(ssr())

for _ in range(t):
    n, m =  map(int, ssr().split())
    if n > m:
        n, m = m, n
    if 2*n >= m:
        if n==m:
            print(n, 3)
        else:
            print(n, 7)
        continue
    if n==1 and m == 3:
        print(2, 5)
        continue
    if 2*n == m-1:
        print(n+1, 7)
        continue
    print(n+1, 2*m-4*n+3)
    