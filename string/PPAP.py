import sys
ssr = sys.stdin.readline

s=list(ssr().strip())

stc=[]

for i in range(len(s)):
    stc.append(s[i])
    while len(stc) > 3:
        if stc[-1]=='P' and stc[-2]=='A' and stc[-3] =='P' and stc[-4]=='P':
            stc.pop()
            stc.pop()
            stc.pop()
            stc.pop()
            stc.append('P')
        else:
            break

if len(stc)==1 and stc[0]=='P':
    print('PPAP')
else:
    print('NP')