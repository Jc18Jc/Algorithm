import sys
ssr = sys.stdin.readline
from collections import deque

s=ssr().strip()
t=ssr().strip()

sblen = 0
tblen = 0
tb = deque()

for i in range(len(s)):
    if s[i]=='B': sblen+=1
for i in range(len(t)):
    if t[i]=='B':
        tblen+=1
        tb.append(i)

reverse=False
front=0
if tblen!=sblen and t[0] != 'B':
    exit(print(0))
while sblen < tblen and len(s) < len(t):
    if reverse:
        tmp=tb.pop()
        t=t[:tmp-front]
    else:
        tmp=tb.popleft()
        t=t[tmp-front+1:]
        front=tmp+1
    tblen-=1
    reverse=not reverse

if reverse:
    t=''.join(reversed(t))
if len(s) <= len(t):
    if tblen==0 and sblen==0:
        print(1)
    elif tblen != sblen:
        print(0)
    else:
        tbs=-1
        sbs=-1
        for i in range(len(t)):
            if t[i]=='B':
                tbs=i
                break
        for i in range(len(s)):
            if s[i]=='B':
                sbs=i
                break
        if tbs < sbs:
            print(0)
        elif front==0:
            t=t[:len(s)]
            if t==s:
                print(1)
            else:
                print(0)
        else:
            if len(s)+tbs-sbs > len(t):
                print(0)
            else:
                t=t[tbs-sbs:len(s)+tbs-sbs]
                if t==s:
                    print(1)
                else:
                    print(0)
else:
    print(0)