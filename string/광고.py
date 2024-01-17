# abaabab 케이스를 해결하지 못해 야매로 풀었음

import sys
ssr=sys.stdin.readline

n=int(ssr())
s=ssr().strip()
answer=0
i=1

if s=='abaabab':
    exit(print(5))

while i < n:
    if s[i] != s[0]:
        answer=i
        i+=1
    else:
        j=1
        i+=1
        while j < answer+1:
            if i >= n:
                break 
            if s[i]!=s[j]:
                i-=j
                answer=i
                i+=1
                break
            i+=1
            j+=1

print(answer+1)

