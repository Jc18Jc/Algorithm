import sys
ssr = sys.stdin.readline

n = int(ssr())

sList = []
maxLen = 0
for _ in range(n):
    s = ssr().strip()
    maxLen = maxLen if maxLen > len(s) else len(s)
    sList.append(s)

k = int(ssr())

difSum = [[0, i] for i in range(36)]

for i in range(n):
    s = sList[i]
    for j in range(len(s)-1, -1, -1):
        o = ord(s[len(s)-1-j])
        num = 0
        if 47 < o < 58:
            num=o-48
        elif 64 < o < 91:
            num = o-55
        dif = (35 - num) * (36**j)
        difSum[num][0]+=dif
    
difSum.sort(reverse=True)

changeList = []
for i in range(k):
    changeList.append(difSum[i][1])

total = 0
for i in range(n):
    s = sList[i]
    for j in range(len(s)-1, -1, -1):
        c = s[len(s)-1-j]
        o = ord(c)        
        if 47 < o < 58:
            num=o-48
        elif 64 < o < 91:
            num = o-55
        if num in changeList:
            num = 35
        total += num*(36**j)

divList = []

while total > 35:
    quo = total//36
    rem = total%36
    divList.append(rem)
    total = quo

divList.append(total)

for i in range(len(divList)):
    if divList[i] < 10:
        divList[i]=str(divList[i])
    else:
        divList[i] = chr(divList[i]+55)

divList.reverse()

answer = ''.join(divList)

print(answer)