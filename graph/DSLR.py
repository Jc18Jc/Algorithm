import sys
ssr = sys.stdin.readline
from collections import deque

t=int(ssr())

for _ in range(t):
    start, end = map(int, ssr().split())
    q = deque()
    q.append((start, []))
    check = [True for _ in range(10000)]
    
    while q:
        v=q.popleft()
        num=v[0]
        lis = v[1]
        if num==end:
            for item in lis:
                if item==1:
                    print('D', end='')
                elif item==2:
                    print('S', end='')
                elif item==3:
                    print('L', end='')
                elif item==4:
                    print('R', end='')
            print()
            break
        if check[2*v[0]%10000]:
            q.append((((2*v[0])%10000), lis+[1]))
            check[2*v[0]%10000]=False
        if num==0 and check[9999]:
            q.append((9999, lis+[2]))
            check[9999]=False
        elif num!=0 and check[num-1]:
            q.append((num-1, lis+[2]))
            check[num-1]=False
        d = num//1000
        num2 = num%1000
        num2 *= 10
        num2+=d
        if check[num2]:
            q.append((num2, lis+[3]))
            check[num2]=False
        res = num%10
        num2 = num//10
        num2+=res*1000
        if check[num2]:
            q.append((num2, lis+[4]))
            check[num2]=False