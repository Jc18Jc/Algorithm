import sys
ssr = sys.stdin.readline

n, m = map(int, ssr().split())

def bt(num, cost, l):
    if cost==0:
        print(*l)
        return
    for i in range(num, n+1):
        bt(i, cost-1, l+[i])

for i in range(1, n+1):
    bt(i, m-1, [i])
    