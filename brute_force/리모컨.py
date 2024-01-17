num = input()
numl = len(num)
num=int(num)
n = int(input())
if n == 0:
    exit(print(min(numl, abs(num-100))))
e = list(map(int, input().split()))
if n == 10:
    exit(print(abs(num-100)))


left = num
right = num

flag1=True
flag2=True
count=-1
answer = abs(100-num)

while flag1 and flag2 and count < answer:
    if left > -1:
        flag1=False
        nl = []
        tl=left
        if left==0:
            nl.append(0)
        else:
            while tl > 0:
                nl.append(tl%10)
                tl=tl//10
        for item in nl:
            if item in e:
                left-=1
                flag1=True
                break
    flag2=False
    nl = []
    tr=right
    if right==0:
        nl.append(0)
    else:
        while tr > 0:
            nl.append(tr%10)
            tr=tr//10
    for item in nl:
        if item in e:
            right+=1
            flag2=True
            break
    count+=1

if not flag1:
    left = str(left)
    l = len(left)
    answer = answer if answer < l+count else l+count
if not flag2:
    right = str(right)
    l = len(right)
    answer = answer if answer < l+count else l+count

print(answer)