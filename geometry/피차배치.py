import sys
from heapq import heappop, heappush
ssr = sys.stdin.readline
PI=3.1415926535

def solution(a, b, k):
    c=(a**2+b**2)**(1/2)
    r=(a+b-c)/2
    if k == 1:
        print(PI*(r**2))
        return
    h = []
    id = [(r**2+r**2)**(1/2), ((a-r)**2+r**2)**(1/2), ((b-r)**2+r**2)**(1/2)]
    outline = [r, a-r, b-r]
    for i in range(3):
        t = (r**2+id[i]**2-outline[i]**2)/2/id[i]
        rate = (id[i]-r) / (id[i]-t)
        p=(((r**2-t**2)**(1/2))*2)*rate
        q=id[i]-r
        l=((p/2)**2+q**2)**(1/2)
        r1 = p*q/(l+l+p)
        heappush(h, (-r1, l, p, q))
    answerR = 0
    while k > 1:
        v=heappop(h)
        q = v[3]-(2*-v[0])
        p = v[2]*q/v[3]
        l = v[1]*q/v[3]
        r1 = p*q/(l+l+p)
        heappush(h, (-r1, l, p, q))
        answerR=v[0]
        k-=1
    print(PI*(answerR**2))
    return

t = int(ssr())

for _ in range(t):
    a, b, k = map(int, ssr().split())
    solution(a, b, k)