import sys
ssr = sys.stdin.readline

def check(l):
    m=len(l)
    flag=2
    i=0
    while i < m:
        if flag==2:
            if m-i > 1 and l[i]==0 and l[i+1]==1:
                i+=2
            elif m-i > 2 and l[i]==1 and l[i+1]==0 and l[i+2]==0:
                i+=3
                flag=0
            else:
                print('NOISE')
                return
        elif flag==0:
            if l[i]==0:
                i+=1
            elif l[i]==1:
                i+=1
                flag=1
            else:
                print(i, 'NOISE')
                return
        elif flag==1:
            if m-i > 2 and l[i]==1 and l[i+1]==0 and l[i+2]==0:
                i+=3
                flag=0
            elif l[i]==1:
                i+=1
            elif m-i > 1 and l[i]==0 and l[i+1]==1:
                i+=2
                flag=2
            else:
                print('NOISE')
                return
    if flag==0:
        print('NOISE')
        return
    else:
        print('SUBMARINE')
        return
    
l = list(ssr().strip())
for i in range(len(l)):
    l[i]=int(l[i])
check(l)
