import sys
ssr = sys.stdin.readline

t = input()
p = input()
lt = len(t)
lp = len(p)
next = [0 for _ in range(lp)]

i=1
j=0

while i < lp:
    if p[i] == p[j]:
        next[i]=j+1
        i+=1
        j+=1
        while i < lp and j < lp:
            if p[i]==p[j]:
                next[i]=j+1
            else:
                while j > 0:
                    if p[i]==p[j]:
                        next[i]=j+1
                        break
                    else:
                        j=next[j-1]
                if j==0:
                    break
            i+=1
            j+=1
    else:
        i+=1

i=0
j=0
count=0
lis = []

while i < lt and j < lp:
    if t[i]==p[j]:
        i+=1
        j+=1
        while i < lt and j < lp:
            if t[i]==p[j]:
                i+=1
                j+=1
            else:
                while j > 0:
                    if t[i] == p[j]:
                        i+=1
                        j+=1
                        break
                    else:
                        j=next[j-1]
                if j == 0:
                    break
        if j==lp:
            count+=1
            lis.append(i-j+1)
            j=next[j-1]
    else:
        if j==0:
            i+=1
        else:
            j=next[j-1]
        
print(count)
for item in lis:
    print(item, end=' ')
        