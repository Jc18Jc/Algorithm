import sys
ssr = sys.stdin.readline

n = int(ssr())
numArray = [0]*n

for i in range(n):
    numArray[i]=int(ssr())

stc = []
count = 0
for i in range(n):
    if not stc:
        stc.append((numArray[i], 0))
        continue
    if numArray[i] < stc[-1][0]:
        stc.append((numArray[i], 1))
        count+=1
    elif numArray == stc[-1]:
        stc.append((numArray[i], stc[-1][1]+1))
        count+=stc[-1][1]
    else:
        while stc and stc[-1][0] < numArray[i]:
            stc.pop()
            count+=1
        if stc and stc[-1][0]==numArray[i]:
            stc.append((numArray[i], stc[-1][1]+1))
            count+=stc[-1][1]
        elif stc and stc[-1][0] > numArray[i]:
            stc.append((numArray[i], 1))
            count+=1
        else:
            stc.append((numArray[i], 0))
print(count)