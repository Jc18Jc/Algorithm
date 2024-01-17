import sys
ssr=sys.stdin.readline

while True:
    s=ssr().strip()
    if s=='.':
        break
    answer=0
    i=1
    while i < len(s):
        if s[i] != s[0]:
            answer=i
            i+=1
        else:
            j=0
            while j < answer+1:
                if i >= len(s):
                    answer=i-1
                    break
                if s[i]!=s[j]:
                    i-=j
                    answer=i
                    i+=1
                    break
                i+=1
                j+=1
    print(len(s)//(answer+1))
